from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.product import Product, ProductCreate, ProductUpdate
from services.product_service import (
    list_products,
    get_product,
    create_product,
    update_product,
    delete_product,
)

router = APIRouter()

@router.get("/products", response_model=list[Product], summary="List products", description="Return all products")
def list_all(db: Session = Depends(get_db)):
    return list_products(db)

@router.get("/products/{product_id}", response_model=Product, summary="Get product", description="Return product by id")
def get_one(product_id: int, db: Session = Depends(get_db)):
    obj = get_product(db, product_id)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return obj

@router.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED, summary="Create product", description="Create a new product")
def create(data: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, data)

@router.put("/products/{product_id}", response_model=Product, summary="Update product", description="Update an existing product")
def update(product_id: int, data: ProductUpdate, db: Session = Depends(get_db)):
    obj = update_product(db, product_id, data)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return obj

@router.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete product", description="Delete product by id")
def delete(product_id: int, db: Session = Depends(get_db)):
    ok = delete_product(db, product_id)
    if not ok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)