from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .databases import engine, get_db
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from passlib.context import CryptContext
from .routers import blog, users, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(users.router)


#def get_db():ß
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()

#@app.post('/blog', tags=['Blogs'])
#def create( request: schemas.Blog, db: Session = Depends(get_db)):
#    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
#    db.add(new_blog)
#    db.commit()
#    db.refresh(new_blog)
#    return new_blog


#@app.delete('/blog{id}', tags=['Blogs'])
#def destroy(id, db:Session = Depends(get_db)):
#    blog = db.query(models.Blog).filter(models.Blog.id == id)
#    if not blog.first():
#       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")    
#    blog.delete(synchronize_session=False)
#    db.commit()
#    return 'Blog deleted successfully'
    

#@app.put('/blog{id}', tags=['Blogs'])
#def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
#    blog = db.query(models.Blog).filter(models.Blog.id == id)
#    if not blog.first():
#       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
#    blog.update({'title': request.title, 'body': request.body})
#    db.commit()
#    return 'Blog updated successfully'

#@app.get('/blog', tags=['Blogs'])
#def all(db: Session = Depends(get_db)):
#    blogs = db.query(models.Blog).all()
#    return blogs

#@app.get('/blog/{id}', tags=['Blogs'])
#def show(id, db: Session = Depends(get_db)):
#    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#    if not blog:
#        Response.status_code = status.HTTP_404_NOT_FOUND
#        return{'detail': f"Blog with the id {id} is not available"}
#    return blog

#pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

#@app.post('/user', response_model=schemas.ShowUser, tags=['Users'])
#def create_user(request: schemas.User, db: Session = Depends(get_db)):
#    hashedPassword = pwd_cxt.hash(request.password)
#    new_user = models.User(name = request.name, email = request.email, password = hashedPassword)
#    db.add(new_user)
#    db.commit()
#    db.refresh(new_user)
#    return new_user

#@app.get('/user/{id}', response_model=schemas.ShowUser, tags=['Users'])
#def get_user(id:int, db:Session = Depends(get_db)):
#    user = db.query(models.User).filter(models.User.id == id).first()
#    if not user:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"User with id {id} not found")
#    return user


