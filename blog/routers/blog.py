from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, databases, models, oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog


get_db = databases.get_db
router = APIRouter()

@router.get('/blog', tags=['Blogs'])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)
#    blogs = db.query(models.Blog).all()
#    return blogs

@router.post('/blog', tags=['Blogs'], )
def create( request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)
#    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
#    db.add(new_blog)
#    db.commit()
#    db.refresh(new_blog)
#    return new_blog

@router.delete('/blog{id}', tags=['Blogs'])
def destroy(id:int, db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)

#    blog = db.query(models.Blog).filter(models.Blog.id == id)
#    if not blog.first():
#       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")    
#    blog.delete(synchronize_session=False)
#    db.commit()
#    return 'Blog deleted successfully'
    

@router.put('/blog{id}', tags=['Blogs'])
def update(id:int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request, db)

#    blog = db.query(models.Blog).filter(models.Blog.id == id)
#    if not blog.first():
#       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
#    blog.update({'title': request.title, 'body': request.body})
#    db.commit()
#    return 'Blog updated successfully'

@router.get('/blog/{id}', tags=['Blogs'])
def show(id:int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id,db)
#    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#    if not blog:
#        Response.status_code = status.HTTP_404_NOT_FOUND
#        return{'detail': f"Blog with the id {id} is not available"}
#    return blog
