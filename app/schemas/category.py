from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class BaseCategory(BaseModel):
    name: str = Field(..., min_length=1, max_length=20)
    description: str | None = None


class CategoryCreate(BaseCategory):
    pass


class CategoryUpdate(BaseCategory):
    description: str | None


class CategoryUpdatePartial(BaseModel):
    name: str = Field(default=None, min_length=1, max_length=20)
    description: str | None = None


class CategoryRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    description: str | None
    created_at: datetime
