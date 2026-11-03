from app.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean


class User(Base):

    username: Mapped[str] = mapped_column(String(20), nullable=False)
    # для входа
    email: Mapped[str] = mapped_column(String(254), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
