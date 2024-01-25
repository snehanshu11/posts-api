from fastapi import Depends, status, HTTPException, APIRouter
from ..database import  get_db
from sqlalchemy.orm import Session
from .. import models, schemas, utils

router = APIRouter( tags= ["users"], prefix="/users")

@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
    hashed_pwd= utils.hash(user.password)
    user.password = hashed_pwd
    new_user=models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}", response_model=schemas.UserResponse)
async def get_user(id: int, db: Session = Depends(get_db)):
    user= db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id:{id} was not found")
    return user