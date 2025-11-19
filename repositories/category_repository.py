from sqlalchemy.orm import Session
from models import Category
from schemas.category import CategoryBase

def get_all(db: Session) -> list[Category]:
    return db.query(Category).all()

def get_by_id(db: Session, category_id: int) -> Category | None:
    return db.query(Category).filter(Category.id == category_id).first()

def create(db: Session, data: CategoryBase) -> Category:
    obj = Category(nombre=data.name)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update(db: Session, category_id: int, data: CategoryBase) -> Category | None:
    obj = get_by_id(db, category_id)
    if not obj:
        return None
    obj.nombre = data.name
    db.commit()
    db.refresh(obj)
    return obj

def delete(db: Session, category_id: int) -> bool:
    obj = get_by_id(db, category_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True