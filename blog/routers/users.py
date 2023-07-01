from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import databases, schemas, models
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from ..repository import user

 

router = APIRouter()
get_db = databases.get_db
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/user', response_model=schemas.ShowUser, tags=['Users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request,db) 
    
#    hashedPassword = pwd_cxt.hash(request.password)
#    new_user = models.User(name = request.name, email = request.email, password = hashedPassword)
#    db.add(new_user)
#    db.commit()
#    db.refresh(new_user)
#    return new_user

@router.get('/user/{id}', response_model=schemas.ShowUser, tags=['Users'])
def get_user(id:int, db:Session = Depends(get_db)):
    return user.show(id,db)
#    user = db.query(models.User).filter(models.User.id == id).first()
#    if not user:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"User with id {id} not found")
#    return user