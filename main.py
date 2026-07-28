from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, models
from database import Base, engine, SessionLocal

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
    return "welcome to the store management portal!"


# ================= Laptop routes =================

@app.post("/laptops", response_model=schemas.LaptopResponse)
def create_laptop(laptop: schemas.LaptopCreate, db: Session = Depends(get_db)):
    return crud.create_laptop(db, laptop)


@app.get("/laptops", response_model=list[schemas.LaptopResponse])
def read_laptops(db: Session = Depends(get_db)):
    return crud.get_laptops(db)


@app.get("/laptops/{laptop_id}", response_model=schemas.LaptopResponse)
def read_laptop(laptop_id: int, db: Session = Depends(get_db)):
    laptop = crud.get_laptop(db, laptop_id)
    if not laptop:
        raise HTTPException(status_code=404, detail="Laptop not found")
    return laptop


@app.put("/laptops/{laptop_id}", response_model=schemas.LaptopResponse)
def update_laptop(laptop_id: int, laptop: schemas.LaptopCreate, db: Session = Depends(get_db)):
    updated = crud.update_laptop(db, laptop_id, laptop)
    if not updated:
        raise HTTPException(status_code=404, detail="Laptop not found")
    return updated


@app.delete("/laptops/{laptop_id}")
def delete_laptop(laptop_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_laptop(db, laptop_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Laptop not found")
    return {"message": "Laptop deleted successfully"}


# ================= Mobile routes =================


@app.post("/mobiles", response_model=schemas.MobileResponse)
def create_mobile(mobile: schemas.MobileCreate, db: Session = Depends(get_db)):
    return crud.create_mobile(db, mobile)


@app.get("/mobiles", response_model=list[schemas.MobileResponse])
def read_mobiles(db: Session = Depends(get_db)):
    return crud.get_mobiles(db)


@app.get("/mobiles/{mobile_id}", response_model=schemas.MobileResponse)
def read_mobile(mobile_id: int, db: Session = Depends(get_db)):
    mobile = crud.get_mobile(db, mobile_id)
    if not mobile:
        raise HTTPException(status_code=404, detail="Mobile not found")
    return mobile


@app.put("/mobiles/{mobile_id}", response_model=schemas.MobileResponse)
def update_mobile(mobile_id: int, mobile: schemas.MobileCreate, db: Session = Depends(get_db)):
    updated = crud.update_mobile(db, mobile_id, mobile)
    if not updated:
        raise HTTPException(status_code=404, detail="Mobile not found")
    return updated


@app.delete("/mobiles/{mobile_id}")
def delete_mobile(mobile_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_mobile(db, mobile_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Mobile not found")
    return {"message": "Mobile deleted successfully"}


# ================= Food Menu routes =================


@app.post("/food-menu", response_model=schemas.FoodMenuResponse)
def create_food_item(food: schemas.FoodMenuCreate, db: Session = Depends(get_db)):
    return crud.create_food_item(db, food)


@app.get("/food-menu", response_model=list[schemas.FoodMenuResponse])
def read_food_items(db: Session = Depends(get_db)):
    return crud.get_food_items(db)


@app.get("/food-menu/{food_id}", response_model=schemas.FoodMenuResponse)
def read_food_item(food_id: int, db: Session = Depends(get_db)):
    food = crud.get_food_item(db, food_id)
    if not food:
        raise HTTPException(status_code=404, detail="Food item not found")
    return food


@app.put("/food-menu/{food_id}", response_model=schemas.FoodMenuResponse)
def update_food_item(food_id: int, food: schemas.FoodMenuCreate, db: Session = Depends(get_db)):
    updated = crud.update_food_item(db, food_id, food)
    if not updated:
        raise HTTPException(status_code=404, detail="Food item not found")
    return updated


@app.delete("/food-menu/{food_id}")
def delete_food_item(food_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_food_item(db, food_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Food item not found")
    return {"message": "Food item deleted successfully"}


# ================= Furniture routes =================


@app.post("/furniture", response_model=schemas.FurnitureResponse)
def create_furniture(furniture: schemas.FurnitureCreate, db: Session = Depends(get_db)):
    return crud.create_furniture(db, furniture)


@app.get("/furniture", response_model=list[schemas.FurnitureResponse])
def read_furniture_list(db: Session = Depends(get_db)):
    return crud.get_furniture_list(db)


@app.get("/furniture/{furniture_id}", response_model=schemas.FurnitureResponse)
def read_furniture(furniture_id: int, db: Session = Depends(get_db)):
    furniture = crud.get_furniture(db, furniture_id)
    if not furniture:
        raise HTTPException(status_code=404, detail="Furniture item not found")
    return furniture


@app.put("/furniture/{furniture_id}", response_model=schemas.FurnitureResponse)
def update_furniture(furniture_id: int, furniture: schemas.FurnitureCreate, db: Session = Depends(get_db)):
    updated = crud.update_furniture(db, furniture_id, furniture)
    if not updated:
        raise HTTPException(status_code=404, detail="Furniture item not found")
    return updated


@app.delete("/furniture/{furniture_id}")
def delete_furniture(furniture_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_furniture(db, furniture_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Furniture item not found")
    return {"message": "Furniture item deleted successfully"}


# ================= Grocery routes =================

@app.post("/grocery", response_model=schemas.GroceryResponse)
def create_grocery(grocery: schemas.GroceryCreate, db: Session = Depends(get_db)):
    return crud.create_grocery(db, grocery)


@app.get("/grocery", response_model=list[schemas.GroceryResponse])
def read_groceries(db: Session = Depends(get_db)):
    return crud.get_groceries(db)


@app.get("/grocery/{grocery_id}", response_model=schemas.GroceryResponse)
def read_grocery(grocery_id: int, db: Session = Depends(get_db)):
    grocery = crud.get_grocery(db, grocery_id)
    if not grocery:
        raise HTTPException(status_code=404, detail="Grocery item not found")
    return grocery


@app.put("/grocery/{grocery_id}", response_model=schemas.GroceryResponse)
def update_grocery(grocery_id: int, grocery: schemas.GroceryCreate, db: Session = Depends(get_db)):
    updated = crud.update_grocery(db, grocery_id, grocery)
    if not updated:
        raise HTTPException(status_code=404, detail="Grocery item not found")
    return updated


@app.delete("/grocery/{grocery_id}")
def delete_grocery(grocery_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_grocery(db, grocery_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Grocery item not found")
    return {"message": "Grocery item deleted successfully"}
