from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=20)
    description: str | None = None
    price: Decimal = Field(..., ge=0, max_digits=10, decimal_places=2)
    stock: int = Field(default=0, ge=0)
    sku: str = Field(..., min_length=1, max_length=10)
    is_active: bool = True


class ProductUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=20)
    description: str | None
    price: Decimal = Field(..., ge=0, max_digits=10, decimal_places=2)
    stock: int = Field(..., ge=0)
    sku: str = Field(..., min_length=1, max_length=10)
    is_active: bool


class ProductUpdatePartial(BaseModel):
    name: str = Field(default=None, min_length=1, max_length=20)
    description: str | None = None
    price: Decimal = Field(default=None, ge=0, max_digits=10, decimal_places=2)
    stock: int = Field(default=None, ge=0)
    is_active: bool = None


class ProductRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str | None
    price: Decimal
    stock: int
    sku: str
    is_active: bool
    created_at: datetime
