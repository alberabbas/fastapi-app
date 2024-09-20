from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..import models, schemas
from ..hashing import Hash


def create_user(request : schemas.Blog, db : Session):
    new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))#define seperately like this
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id:int, db : Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found') 
    return user