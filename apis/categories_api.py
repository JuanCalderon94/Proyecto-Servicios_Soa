from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.category import Category, CategoryBase
from services.category_service import (
    list_categories,
    get_category,
    create_category,
    update_category,
    delete_category,
)

router = APIRouter()

@router.get("/categories", response_model=list[Category], summary="List categories", description="Return all categories")
def list_all(db: Session = Depends(get_db)):
    return list_categories(db)

@router.get("/categories/{category_id}", response_model=Category, summary="Get category", description="Return category by id")
def get_one(category_id: int, db: Session = Depends(get_db)):
    obj = get_category(db, category_id)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return obj

@router.post("/categories", response_model=Category, status_code=status.HTTP_201_CREATED, summary="Create category", description="Create a new category")
def create(data: CategoryBase, db: Session = Depends(get_db)):
    return create_category(db, data)

@router.put("/categories/{category_id}", response_model=Category, summary="Update category", description="Update an existing category")
def update(category_id: int, data: CategoryBase, db: Session = Depends(get_db)):
    obj = update_category(db, category_id, data)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return obj

@router.delete("/categories/{category_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete category", description="Delete category by id")
def delete(category_id: int, db: Session = Depends(get_db)):
    ok = delete_category(db, category_id)
    if not ok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)