from pydantic import BaseModel


# ---------- Laptop --------
class LaptopCreate(BaseModel):
    brand: str
    model: str
    price: int
    ram_gb: int


class LaptopResponse(LaptopCreate):
    id: int

    model_config = {
        "from_attributes": True
    }


# ---------- Mobile ----------
class MobileCreate(BaseModel):
    brand: str
    model: str
    price: int
    storage_gb: int


class MobileResponse(MobileCreate):
    id: int

    model_config = {
        "from_attributes": True
    }


# ---------- FoodMenu ----------
class FoodMenuCreate(BaseModel):
    item_name: str
    category: str
    price: int
    calories: int


class FoodMenuResponse(FoodMenuCreate):
    id: int

    model_config = {
        "from_attributes": True
    }


# ---------- Furniture ----------
class FurnitureCreate(BaseModel):
    name: str
    material: str
    price: int
    dimensions: str


class FurnitureResponse(FurnitureCreate):
    id: int

    model_config = {
        "from_attributes": True
    }


# ---------- Grocery ----------
class GroceryCreate(BaseModel):
    item_name: str
    category: str
    price: int
    quantity: int


class GroceryResponse(GroceryCreate):
    id: int

    model_config = {
        "from_attributes": True
    }