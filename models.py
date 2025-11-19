from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Product(Base):
    __tablename__ = "producto"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(150), nullable=False)
    cantidad: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

class Category(Base):
    __tablename__ = "categoria"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(150), nullable=False)