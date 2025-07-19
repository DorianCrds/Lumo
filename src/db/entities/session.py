# db/entities/session.py
from sqlalchemy import Column, Integer, DateTime
from src.db.entities.base import Base

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    break_minutes = Column(Integer, default=0)
