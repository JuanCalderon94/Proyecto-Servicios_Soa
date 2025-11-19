from sqlalchemy.orm import Session
from models import Product
from schemas.product import ProductCreate, ProductUpdate

def get_all(db: Session) -> list[Product]:
    return db.query(Product).all()

def get_by_id(db: Session, product_id: int) -> Product | None:
    return db.query(Product).filter(Product.id == product_id).first()

def create(db: Session, data: ProductCreate) -> Product:
    obj = Product(nombre=data.name, cantidad=data.quantity)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update(db: Session, product_id: int, data: ProductUpdate) -> Product | None:
    obj = get_by_id(db, product_id)
    if not obj:
        return None
    if data.name is not None:
        obj.nombre = data.name
    if data.quantity is not None:
        obj.cantidad = data.quantity
    db.commit()
    db.refresh(obj)
    return obj

def delete(db: Session, product_id: int) -> bool:
    obj = get_by_id(db, product_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True