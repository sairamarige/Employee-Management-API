from sqlalchemy import Column, Integer, String, Float
from database import Base


class Laptop(Base):
    __tablename__ = "laptops"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    ram_gb = Column(Integer, nullable=False)


class Mobile(Base):
    __tablename__ = "mobiles"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    storage_gb = Column(Integer, nullable=False)


class FoodMenu(Base):
    __tablename__ = "food_menu"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)
    price = Column(Integer, nullable=False)
    calories = Column(Integer, nullable=False)


class Furniture(Base):
    __tablename__ = "furniture"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    material = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    dimensions = Column(String(50), nullable=False)


class Grocery(Base):
    __tablename__ = "grocery"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
