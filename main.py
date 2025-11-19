from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from apis.products_api import router as products_router
from apis.categories_api import router as categories_router
from database import Base, engine
import models

app = FastAPI()
app.include_router(products_router, prefix="/api", tags=["product"])
app.include_router(categories_router, prefix="/api", tags=["category"])

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return RedirectResponse(url="/docs")