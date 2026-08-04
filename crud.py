from sqlalchemy.orm import Session
import models
import schemas
import bcrypt
import jwt
from fastapi import Response

SECRET_KEY = "abcdefghijklmnopqrtuvwxyz"
ALGORITHM = "HS256"


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def get_employees(db: Session):
    return db.query(models.Employee).all()


def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()


def get_by_department(db: Session, department: str):
    return db.query(models.Employee).filter(
        models.Employee.department == department
    ).all()


def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeCreate):
    db_employee = get_employee(db, employee_id)
    if not db_employee:
        return None
    db_employee.name = employee.name
    db_employee.age = employee.age
    db_employee.department = employee.department
    db_employee.email = employee.email
    db.commit()
    db.refresh(db_employee)
    return db_employee


def patch_employee(db: Session, employee_id: int, fields: dict):
    db_employee = get_employee(db, employee_id)
    if not db_employee:
        return None
    for key, value in fields.items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, employee_id: int):
    db_employee = get_employee(db, employee_id)
    if not db_employee:
        return None
    db.delete(db_employee)
    db.commit()
    return db_employee


def create_user(user: schemas.UserCreate, db: Session):
    # If an employee_id was given, make sure it actually points to a real
    # employee, and that employee doesn't already have a login account.
    if user.employee_id is not None:
        employee = get_employee(db, user.employee_id)
        if not employee:
            return {"error": "No employee found with that employee_id"}
        existing_link = db.query(models.User).filter(
            models.User.employee_id == user.employee_id
        ).first()
        if existing_link:
            return {"error": "This employee already has a login account"}

    hashed = bcrypt.hashpw(
        user.password.encode(),  # input should be in bytes
        bcrypt.gensalt(rounds=14)
    ).decode("utf-8")

    new_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed,
        role=user.role,
        employee_id=user.employee_id
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def validate_user(user: schemas.UserLogin, db: Session, response: Response):
    user_exist = db.query(models.User).filter(models.User.email == user.email).first()
    if not user_exist:
        return "no user found"

    is_same = bcrypt.checkpw(user.password.encode(), user_exist.hashed_password.encode())
    if is_same:
        payload = {
            "name": user_exist.username,
            "email": user_exist.email,
            "role": user_exist.role
        }
        token = jwt.encode(payload, SECRET_KEY, ALGORITHM)
        response.set_cookie(key="access_token", value=token)
        return "login successful!"

    return "invalid credentials"

    

    

   

   
   
