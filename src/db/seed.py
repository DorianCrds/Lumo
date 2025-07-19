# db/seed.py

from datetime import datetime, timedelta
import random

from src.db.entities.base import Base
from src.db.entities.session import Session as WorkSession
from src.db.database import engine, SessionLocal

def seed_sessions(n_days=10):
    Base.metadata.create_all(engine)

    db = SessionLocal()

    db.query(WorkSession).delete()

    base_date = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)

    for i in range(n_days):
        day = base_date - timedelta(days=i)
        for _ in range(random.randint(1, 2)):
            start_hour = random.randint(8, 10)
            duration = random.randint(60, 180)
            break_minutes = random.choice([0, 5, 10, 15])

            start = day.replace(hour=start_hour)
            end = start + timedelta(minutes=duration)

            s = WorkSession(
                start_time=start,
                end_time=end,
                break_minutes=break_minutes
            )
            db.add(s)

    db.commit()
    db.close()
    print(f"{n_days} jours de sessions créés.")
