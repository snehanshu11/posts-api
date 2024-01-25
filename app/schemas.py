from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional

class Post(BaseModel):
    title: str
    details: str
    published: bool = True

class PostCreate(Post):
    pass

class User(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    created_at: datetime
    id: int
    email: EmailStr
    class Config:
        from_attributes = True

class PostResponse(Post):
    created_at: datetime
    id: int
    owner_id: int
    owner: UserResponse
    class Config:
        from_attributes = True

class PostVote(BaseModel):
    Post: PostResponse
    votes: int

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] 


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
