from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from decimal import Decimal
from sqlalchemy import String, Numeric, Integer, Boolean, Text


class Category(Base):
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    products: Mapped[list["Products"]] = relationship(back_populates="category")
