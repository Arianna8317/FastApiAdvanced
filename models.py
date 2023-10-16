from pydantic import BaseModel, Field
from datetime import date

class User(BaseModel):
    id: int
    name: str = Field(..., max_length=32)
    email: str = Field(..., max_length=128)

class UserIn(BaseModel):
    name: str = Field(..., min_length=2)
    surname: str = Field(..., min_length=2)
    birthday: date = Field(..., format="%Y-%m-%d")
    adress: str = Field(..., )
    email: str = Field(..., max_length=128)
    password: str = Field(..., min_length=6)

class Product(BaseModel):
    id: int
    name: str = Field(..., max_length=32)
    description: str = Field(..., max_length=128)
    price: int

class ProductIn(BaseModel):
    name: str = Field(..., min_length=2)
    description: str = Field(..., max_length=128)
    price: int

class Order(BaseModel):
    id: int
    user_id: int
    product_id: str = Field(..., max_length=32)
    creation_date: date = Field(..., format="%Y-%m-%d")
    description: str = Field(..., max_length=128)
    status: bool

class OrderIn(BaseModel):
    user_id: int
    product_id: str = Field(..., max_length=32)
    creation_date: date = Field(..., format="%Y-%m-%d")
    description: str = Field(..., max_length=128)
    status: bool