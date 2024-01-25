from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm 
from sqlalchemy.orm import Session
from ..database import  get_db
from .. import schemas, models, utils, oauth2


router = APIRouter(prefix="/login",tags=["authentication"])

@router.post("/", response_model=schemas.Token)
async def login(user_credentials: OAuth2PasswordRequestForm =  Depends() , db: Session = Depends(get_db)):
    user = db.query(models.User).filter(user_credentials.username == models.User.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    # verify if the password provided by user is equal to what we have in database. Convert the provided password into hash and compare
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    # create a token and return it
    access_token = oauth2.create_access_token(data = {"user_id": user.id})

    return {"access_token":access_token, "token_type": "bearer"}
