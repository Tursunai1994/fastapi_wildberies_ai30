from fastapi import APIRouter,Depends,HTTPException, status
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import Review
from db.schema import ReviewCreateSchema,ReviewListSchema
from typing import List


review_router = APIRouter(prefix='/review',tags=['Review'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@review_router.post('/create',response_model=ReviewCreateSchema)
async def create_review(review_data:ReviewCreateSchema,db: Session = Depends(get_db)):
    review_db = Review(**review_data.dict())
    db.add(review_db)
    db.commit()
    db.refresh(review_db)
    return review_db

@review_router.get('/list',response_model=List[ReviewListSchema])
async def list_review(db: Session = Depends(get_db)):
    review_db = db.query(Review).all()
    return review_db



















