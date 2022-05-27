from pydantic import BaseModel, Field


class Employee(BaseModel):
    __tablename__ = "employee"
    
    employee_id: int
    employee_name: str = Field(..., min_length=3, max_length=50)
    class Config:
        orm_mode=True