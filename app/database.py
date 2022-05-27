from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a sqlite engine instance
engine = create_engine("sqlite:///todooo.db")

# Create a DeclarativeMeta instance
Base = declarative_base()

# Define To Do class inheriting from Base
class EmployeeDb(Base):
    __tablename__ = 'employee'
    employee_id = Column(Integer, primary_key=True)
    employee_name = Column(String(256))


