# models/session_model.py
from src.db.database import SessionLocal
from src.db.entities.session import Session
from datetime import timedelta

class SessionModel:
    def __init__(self, db=None):
        self.db = db or SessionLocal()

    def add_session(self, start_time, end_time, break_minutes=0):
        new_session = Session(
            start_time=start_time,
            end_time=end_time,
            break_minutes=break_minutes
        )
        self.db.add(new_session)
        self.db.commit()

    def delete_session(self, session_id):
        session = self.db.query(Session).get(session_id)
        if session:
            self.db.delete(session)
            self.db.commit()

    def get_all_sessions(self):
        sessions = self.db.query(Session).order_by(Session.start_time.desc()).all()
        return [self._to_dict(s) for s in sessions]

    def _to_dict(self, session):
        duration = session.end_time - session.start_time - timedelta(minutes=session.break_minutes)
        return {
            "id": session.id,
            "start_time": session.start_time,
            "end_time": session.end_time,
            "break_minutes": session.break_minutes,
            "duration": duration,
            "duration_str": str(self.format_timedelta(duration))
        }

    def get_total_worked_time(self):
        sessions = self.db.query(Session).all()
        total = timedelta()
        for s in sessions:
            total += s.end_time - s.start_time - timedelta(minutes=s.break_minutes)
        return total

    def get_stats(self, period="toutes"):
        from datetime import datetime

        now = datetime.now()
        sessions = self.db.query(Session).all()

        # Filtrage par période
        if period == "semaine":
            start_date = now - timedelta(days=now.weekday())  # début de semaine
            sessions = [s for s in sessions if s.start_time.date() >= start_date.date()]
        elif period == "mois":
            start_date = now.replace(day=1)  # début du mois
            sessions = [s for s in sessions if s.start_time.date() >= start_date.date()]

        # Calcul des stats (identique)
        if not sessions:
            return {
                "days_worked": 0,
                "total_worked_time": timedelta(0),
                "average_per_day": timedelta(0),
                "total_worked_time_str": "0h 0min",
                "average_per_day_str": "0h 0min",
            }

        total_time = timedelta()
        days = set()

        for s in sessions:
            duration = s.end_time - s.start_time - timedelta(minutes=s.break_minutes)
            total_time += duration
            days.add(s.start_time.date())

        days_worked = len(days)
        average_per_day = total_time / days_worked if days_worked else timedelta(0)

        return {
            "days_worked": days_worked,
            "total_worked_time": total_time,
            "average_per_day": average_per_day,
            "total_worked_time_str": self.format_timedelta(total_time),
            "average_per_day_str": self.format_timedelta(average_per_day),
        }

    @staticmethod
    def format_timedelta(td):
        total_seconds = int(td.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        return f"{hours}h {minutes}min"
