from pydantic import BaseModel
from typing import Literal, Optional

Role = Literal["intern", "dev", "manager"]


class EmployeeCreate(BaseModel):
    name: str
    age: int
    department: str
    email: str


class EmployeeUpdate(BaseModel):
    """Used for PATCH - every field optional so only sent fields get changed."""
    name: Optional[str] = None
    age: Optional[int] = None
    department: Optional[str] = None
    email: Optional[str] = None


class EmployeeResponse(EmployeeCreate):
    id: int

    model_config = {
        "from_attributes": True
    }


class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    role: Role = "intern"
    employee_id: Optional[int] = None  # link this login to an existing employee record


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: Role
    employee_id: Optional[int] = None

    model_config = {
        "from_attributes": True
    }










