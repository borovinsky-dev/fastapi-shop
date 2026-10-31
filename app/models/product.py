from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from decimal import Decimal
from sqlalchemy import String, Numeric, Integer, Boolean, Text


class Product(Base):
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    # остаток
    stock: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    # артикул
    sku: Mapped[str] = mapped_column(
        String(10), unique=True, index=True, nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
