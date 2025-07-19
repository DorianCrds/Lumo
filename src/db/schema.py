# db/schema.py
from src.db.database import engine
from src.db.entities.base import Base

def initialize_database():
    Base.metadata.create_all(bind=engine)
