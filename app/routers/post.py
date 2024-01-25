from fastapi import  Depends, status, HTTPException, APIRouter
from sqlalchemy import func
from ..database import  get_db
from typing import Optional
from sqlalchemy.orm import Session
from .. import models, schemas, oauth2

router=APIRouter(tags=["posts"], prefix="/posts")

@router.get("/",response_model=list[schemas.PostVote])
#@router.get("/")
async def get_posts(db: Session = Depends(get_db),current_user: str = Depends(oauth2.get_current_user), limit:str=5, offset:str=0, search:Optional[str] =""):
    #posts= db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(offset).all()
    results = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Post.id==models.Vote.post_id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(offset).all()
    #print(current_user.email)
    return  results

@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
async def create_post(post: schemas.PostCreate,db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    #new_post=models.Post(title=post.title, content=post.details,published=post.published)
    #print(user_id)
    new_post=models.Post(owner_id=current_user.id,**post.model_dump())
    db.add(new_post)
    db.commit() 
    db.refresh(new_post)
    return new_post

@router.get("/{id}", response_model=schemas.PostVote)
async def get_one_post(id: int, db: Session = Depends(get_db),current_user: str = Depends(oauth2.get_current_user)):
    #post = db.query(models.Post).filter(models.Post.id == id).first()
    post = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Post.id==models.Vote.post_id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} was not found")
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:int, db: Session = Depends(get_db),current_user: str = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} was not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")
    post_query.delete(synchronize_session=False)
    db.commit()
    return {"msg": "Post deleted"}

@router.put("/{id}", response_model=schemas.PostResponse)
async def delete_post(post: schemas.PostCreate, id:int, db: Session = Depends(get_db),current_user: str = Depends(oauth2.get_current_user)):
    post_to_update = db.query(models.Post).filter(models.Post.id == id)
    post = post_to_update.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} was not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")
    post_to_update.update(post.model_dump(),synchronize_session=False)
    db.commit()
    return post_to_update.first()    





