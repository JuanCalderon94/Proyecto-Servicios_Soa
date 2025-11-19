from pydantic import BaseModel, Field
from pydantic.config import ConfigDict

class CategoryBase(BaseModel):
    name: str

class Category(BaseModel):
    id: int
    name: str = Field(validation_alias="nombre")
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)