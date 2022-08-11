from pydantic import BaseModel
from typing import Optional,List
from datetime import datetime

class TodoBase(BaseModel):
  title:str
  description:str
  completed:bool

class TodoCreate(TodoBase):
  user_id:int

class TodoPut(TodoBase):
  title:Optional[str]
  description:Optional[str]
  completed:Optional[bool]

# Properties shared by models stored in DB
class TodoInDb(TodoBase):
  id:int
  user_id:int
  created:datetime
  class Config:
    orm_mode = True
# Properties to return to client
class TodoRead(TodoInDb):
  pass
  class Config:
        orm_mode = True

class UserBase(BaseModel):
  username:str
  email:str
class UserCreate(UserBase):
  pass

class UserInfo(UserBase):
  id:int
  is_active:bool
  class Config:
    orm_mode = True

class UserRead(UserInfo):
  todos:List[TodoRead] = []
  class Config:
    orm_mode = True

class UserPut(UserBase):
  username:Optional[str]
  email:Optional[str]
  is_active:Optional[bool]



