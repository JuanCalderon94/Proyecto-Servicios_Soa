from sqlalchemy.orm import Session
from schemas.category import CategoryBase, Category
from repositories.category_repository import (
    get_all,
    get_by_id,
    create as repo_create,
    update as repo_update,
    delete as repo_delete,
)

def list_categories(db: Session) -> list[Category]:
    return get_all(db)

def get_category(db: Session, category_id: int) -> Category | None:
    return get_by_id(db, category_id)

def create_category(db: Session, data: CategoryBase) -> Category:
    return repo_create(db, data)

def update_category(db: Session, category_id: int, data: CategoryBase) -> Category | None:
    return repo_update(db, category_id, data)

def delete_category(db: Session, category_id: int) -> bool:
    return repo_delete(db, category_id)