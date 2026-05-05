from fastapi import APIRouter,Depends,HTTPException, status
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import Product
from db.schema import ProductCreateSchema,ProductListSchema,ProductDetailSchema
from typing import List


product_router = APIRouter(prefix='/product',tags=['Product'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@product_router.post('/create',response_model=ProductCreateSchema)
async def create_product(product_data:ProductCreateSchema,db: Session = Depends(get_db)):
    product_db = Product(**product_data.dict())
    db.add(product_db)
    db.commit()
    db.refresh(product_db)
    return product_db

@product_router.get('/list',response_model=List[ProductListSchema])
async def list_product(db: Session = Depends(get_db)):
    product_db = db.query(Product).all()
    return product_db

@product_router.get('/detail/{product_id}',response_model=ProductDetailSchema)
async def detail_product(product_id:int, db: Session = Depends(get_db)):
    product_db = db.query(Product).filter(Product.id == product_id).first()
    if not product_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Munday adam jok')
    return product_db


















