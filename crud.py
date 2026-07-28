from sqlalchemy.orm import Session
import models
import schemas


#============Laptop===========
def create_laptop(db:Session,laptop: schemas.LaptopCreate):
    db_laptop=models.Laptop(**laptop.model_dump())
    db.add(db_laptop)
    db.commit()
    db.refresh(db_laptop)
    return db_laptop


def get_laptops(db:Session):
    return db.query(models.Laptop).all()


def get_laptop(db:Session,laptop_id:int):
    return db.query(models.Laptop).filter(models.Laptop.id == laptop_id).first()


def update_laptop(db:Session,laptop_id:int,laptop: schemas.LaptopCreate):
    db_laptop=get_laptop(db,laptop_id)
    if not db_laptop:
        return None
    db_laptop.brand= laptop.brand
    db_laptop.model=laptop.model
    db_laptop.price=laptop.price
    db_laptop.ram_gb=laptop.ram_gb
    db.commit()
    db.refresh(db_laptop)
    return db_laptop


def delete_laptop(db:Session,laptop_id:int):
    db_laptop = get_laptop(db,laptop_id)
    if not db_laptop:
        return None
    db.delete(db_laptop)
    db.commit()
    return db_laptop


#=============Mobile==============
def create_mobile(db:Session,mobile:schemas.MobileCreate):
    db_mobile=models.Mobile(**mobile.model_dump())
    db.add(db_mobile)
    db.commit()
    db.refresh(db_mobile)
    return db_mobile


def get_mobiles(db:Session):
    return db.query(models.Mobile).all()


def get_mobile(db:Session,mobile_id:int):
    return db.query(models.Mobile).filter(models.Mobile.id == mobile_id).first()


def update_mobile(db:Session,mobile_id:int,mobile: schemas.MobileCreate):
    db_mobile=get_mobile(db,mobile_id)
    if not db_mobile:
        return None
    db_mobile.brand=mobile.brand
    db_mobile.model=mobile.model
    db_mobile.price=mobile.price
    db_mobile.storage_gb=mobile.storage_gb
    db.commit()
    db.refresh(db_mobile)
    return db_mobile


def delete_mobile(db:Session,mobile_id:int):
    db_mobile=get_mobile(db, mobile_id)
    if not db_mobile:
        return None
    db.delete(db_mobile)
    db.commit()
    return db_mobile


#================FoodMenu=================
def create_food_item(db:Session,food:schemas.FoodMenuCreate):
    db_food=models.FoodMenu(**food.model_dump())
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food


def get_food_items(db:Session):
    return db.query(models.FoodMenu).all()


def get_food_item(db:Session,food_id:int):
    return db.query(models.FoodMenu).filter(models.FoodMenu.id==food_id).first()


def update_food_item(db:Session,food_id:int,food:schemas.FoodMenuCreate):
    db_food = get_food_item(db, food_id)
    if not db_food:
        return None
    db_food.item_name = food.item_name
    db_food.category = food.category
    db_food.price = food.price
    db_food.calories = food.calories
    db.commit()
    db.refresh(db_food)
    return db_food


def delete_food_item(db: Session, food_id: int):
    db_food = get_food_item(db, food_id)
    if not db_food:
        return None
    db.delete(db_food)
    db.commit()
    return db_food


#=================Furniture====================

def create_furniture(db: Session, furniture: schemas.FurnitureCreate):
    db_furniture = models.Furniture(**furniture.model_dump())
    db.add(db_furniture)
    db.commit()
    db.refresh(db_furniture)
    return db_furniture


def get_furniture_list(db: Session):
    return db.query(models.Furniture).all()


def get_furniture(db: Session, furniture_id: int):
    return db.query(models.Furniture).filter(models.Furniture.id == furniture_id).first()


def update_furniture(db: Session, furniture_id: int, furniture: schemas.FurnitureCreate):
    db_furniture = get_furniture(db, furniture_id)
    if not db_furniture:
        return None
    db_furniture.name = furniture.name
    db_furniture.material = furniture.material
    db_furniture.price = furniture.price
    db_furniture.dimensions = furniture.dimensions
    db.commit()
    db.refresh(db_furniture)
    return db_furniture


def delete_furniture(db: Session, furniture_id: int):
    db_furniture = get_furniture(db, furniture_id)
    if not db_furniture:
        return None
    db.delete(db_furniture)
    db.commit()
    return db_furniture


# ================= Grocery =================
def create_grocery(db: Session, grocery: schemas.GroceryCreate):
    db_grocery = models.Grocery(**grocery.model_dump())
    db.add(db_grocery)
    db.commit()
    db.refresh(db_grocery)
    return db_grocery

def get_groceries(db: Session):
    return db.query(models.Grocery).all()


def get_grocery(db: Session, grocery_id: int):
    return db.query(models.Grocery).filter(models.Grocery.id == grocery_id).first()


def update_grocery(db: Session, grocery_id: int, grocery: schemas.GroceryCreate):
    db_grocery = get_grocery(db, grocery_id)
    if not db_grocery:
        return None
    db_grocery.item_name = grocery.item_name
    db_grocery.category = grocery.category
    db_grocery.price = grocery.price
    db_grocery.quantity = grocery.quantity
    db.commit()
    db.refresh(db_grocery)
    return db_grocery



def delete_grocery(db: Session, grocery_id: int):
    db_grocery = get_grocery(db, grocery_id)
    if not db_grocery:
        return None
    db.delete(db_grocery)
    db.commit()
    return db_grocery
