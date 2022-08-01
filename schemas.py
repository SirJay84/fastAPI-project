from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TodoBase(BaseModel):
  id:Optional[int] = None
  title:str
  description:str
  completed:bool
  created:Optional[datetime] = None

class TodoCreate(TodoBase):
  completed:bool

class TodoPut(TodoBase):
  title:Optional[str]
  description:Optional[str]
  completed:Optional[bool]

class Todo(TodoBase):
  id:int
  completed:bool
  created:datetime