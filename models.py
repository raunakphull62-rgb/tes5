python
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: str
    email: str
    name: str

class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float
    user_id: str

class CreateUser(BaseModel):
    email: str
    password: str
    name: str

class CreateProduct(BaseModel):
    name: str
    description: str
    price: float
    user_id: str

class UpdateUser(BaseModel):
    email: Optional[str]
    name: Optional[str]

class UpdateProduct(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]