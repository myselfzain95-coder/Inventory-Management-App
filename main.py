from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db, engine, SessionLocal
from models import Product, Base
from pydantic import BaseModel
from typing import Optional

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProductSchema(BaseModel):
    name:        str
    description: Optional[str] = ""
    price:       float
    quantity:    int

def get_or_404(db: Session, id: int) -> Product:
    product = db.query(Product).filter(Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

def init_db():
    db = SessionLocal()
    if db.query(Product).count() == 0:
        products = [
            Product(name="Laptop", description="Gaming laptop", price=1500.00, quantity=10),
            Product(name="Mouse", description="Wireless mouse", price=25.00, quantity=50),
            Product(name="Keyboard", description="Mechanical keyboard", price=75.00, quantity=30),
        ]
        for product in products:
            db.add(product)
        db.commit()
    db.close()

init_db()

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@app.post("/products")
def create_product(data: ProductSchema, db: Session = Depends(get_db)):
    product = Product(**data.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

@app.put("/products/{id}")
def update_product(id: int, data: ProductSchema, db: Session = Depends(get_db)):
    product = get_or_404(db, id)
    for key, value in data.dict().items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    product = get_or_404(db, id)
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}