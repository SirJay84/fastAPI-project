from fastapi import APIRouter,Depends,HTTPException
from typing import Dict,List,Generator
from sqlalchemy.orm import Session
from db.session import SessionLocal
from models.user import User
from schemas import UserRead,UserCreate,UserPut,UserInfo

#In memory db
db = []

#dependency function
def get_db() -> Generator:
    try:
        db= SessionLocal()
        yield db
    finally:
        db.close()

user_router = APIRouter()

#get all users
@user_router.get('/',
response_model=List[UserInfo],
summary = 'All users',
status_code=200)
def users(db:Session = Depends(get_db), skip:int=0, limit:int=10):
  users = db.query(User).offset(skip).limit(limit).all()
  return users
  
#get single user
@user_router.get('/{userID}',
response_model=UserRead,
summary='Get a single user',
status_code=200)
def get_user(userID:int, db:Session = Depends(get_db)):
  db_user = db.query(User).filter(User.id == userID).first()
  if db_user is None:
    raise HTTPException(status_code=404,detail=f'Woops user id {userID} does not exist.')
  return db_user

#Create a new user
@user_router.post('/',
response_model=UserRead,
summary="Add a User",
status_code=200)
def create_user(user:UserCreate, db:Session = Depends(get_db)):
  db_user = db.query(User).filter(User.email == user.email).first()
  if db_user:
    raise HTTPException(status_code=400,detail=f'{user.email} is already in use!')
  db_user = User(**user.dict())
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user

# Update a user
@user_router.put('/{userID}',
response_model=Dict[str,str],
summary="Update a User",
status_code=200)
def update_user(userID:int, user:UserPut, db:Session = Depends(get_db)):
  db_user = db.query(User).filter(User.id == userID).first()
  if db_user is None:
    raise HTTPException(status_code=404,detail=f'Woops user id {userID} does not exist.')
  db_user.username = user.username
  db_user.email = user.email
  db_user.is_active = user.is_active
  db.commit()
  return {'message':f"User id:{userID} has been successfully updated."}

# Delete a user
@user_router.delete('/{userID}',
response_model=Dict[str,str],
summary="Delete a User",
status_code=200)
def delete_user(userID:int,db:Session = Depends(get_db)):
  db_user = db.query(User).filter(User.id == userID).first()
  if db_user is None:
    raise HTTPException(status_code=404,detail=f'Woops user id {userID} does not exist.')
  db.delete(db_user)
  db.commit()
  return {'message':f"User id:{userID} has been successfully deleted."}

"""Dependency Injection (DI) is a way functions and classes declare things they need to work ."""
"""In FastAPI context ,endpoint functions are called path operation functions."""






