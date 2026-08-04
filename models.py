from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    department = Column(String(100), nullable=False)
    email = Column(String(50), unique=True, nullable=True)

    # One employee can have one login account (optional - not every employee
    # necessarily gets a login, and not every user is necessarily an employee).
    user = relationship("User", back_populates="employee", uselist=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    hashed_password = Column(String(300), nullable=False)
    role = Column(String(20), nullable=False, default="intern")  # intern | dev | manager
    is_active = Column(Boolean, default=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    # Links this login account to an employee record (nullable - lets you
    # still create staff accounts, e.g. a manager, with no employee row).
    employee_id = Column(Integer, ForeignKey("employees.id"), unique=True, nullable=True)
    employee = relationship("Employee", back_populates="user")
