from pydantic import BaseModel, Field
from pydantic.config import ConfigDict

class ProductBase(BaseModel):
    name: str
    quantity: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: str | None = None
    quantity: int | None = None

class Product(BaseModel):
    id: int
    name: str = Field(validation_alias="nombre")
    quantity: int = Field(validation_alias="cantidad")
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)