from fastapi import FastAPI, Depends, HTTPException, Response
from sqlalchemy.orm import Session
import crud, schemas
from database import Base, engine, SessionLocal
import auth

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def welcome():
    return "welcome to employee management portal!"


@app.get("/employees", response_model=list[schemas.EmployeeResponse])
def read_all(
    db: Session = Depends(get_db),
    user=Depends(auth.allow_get)
):
    return crud.get_employees(db)


@app.post("/employees", response_model=schemas.EmployeeResponse)
def create(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db),
    user=Depends(auth.allow_write)
):
    return crud.create_employee(db, employee)


@app.get("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def read_one(
    employee_id: int,
    db: Session = Depends(get_db),
    user=Depends(auth.allow_get)
):
    employee = crud.get_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.put("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def update(
    employee_id: int,
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db),
    user=Depends(auth.allow_write)
):
    updated = crud.update_employee(db, employee_id, employee)
    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated


@app.patch("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def patch(
    employee_id: int,
    employee: schemas.EmployeeUpdate,
    db: Session = Depends(get_db),
    user=Depends(auth.allow_write)
):
    fields = employee.model_dump(exclude_unset=True)
    patched = crud.patch_employee(db, employee_id, fields)
    if not patched:
        raise HTTPException(status_code=404, detail="Employee not found")
    return patched


@app.delete("/employees/{employee_id}")
def delete(
    employee_id: int,
    db: Session = Depends(get_db),
    user=Depends(auth.allow_delete)
):
    deleted = crud.delete_employee(db, employee_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}


@app.get("/department/{department_name}", response_model=list[schemas.EmployeeResponse])
def department_employees(
    department_name: str,
    db: Session = Depends(get_db),
    user=Depends(auth.allow_get)
):
    employee_list = crud.get_by_department(db, department_name)
    if not employee_list:
        raise HTTPException(status_code=404, detail="No employees found in this department!")
    return employee_list


@app.post("/register_user", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    result = crud.create_user(user, db)
    if isinstance(result, dict) and "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result


@app.post("/login")
def login_user(response: Response, user: schemas.UserLogin, db: Session = Depends(get_db)):
    return crud.validate_user(user, db, response)
      

  

   

        
        
