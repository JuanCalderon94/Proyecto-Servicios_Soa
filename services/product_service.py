from sqlalchemy.orm import Session
from schemas.product import ProductCreate, ProductUpdate, Product
from repositories.product_repository import (
    get_all,
    get_by_id,
    create as repo_create,
    update as repo_update,
    delete as repo_delete,
)

def list_products(db: Session) -> list[Product]:
    return get_all(db)

def get_product(db: Session, product_id: int) -> Product | None:
    return get_by_id(db, product_id)

def create_product(db: Session, data: ProductCreate) -> Product:
    return repo_create(db, data)

def update_product(db: Session, product_id: int, data: ProductUpdate) -> Product | None:
    return repo_update(db, product_id, data)

def delete_product(db: Session, product_id: int) -> bool:
    return repo_delete(db, product_id)