from fastapi import APIRouter,Depends,HTTPException
from typing import List,Dict,Generator
from schemas import TodoCreate,TodoRead,TodoPut,TodoInDb
from sqlalchemy.orm import Session
from db.session import SessionLocal
from models.todo import Todo
from models.user import User

#In memory db
db = []

#dependency function
def get_db() -> Generator:
    try:
        db= SessionLocal()
        yield db
    finally:
        db.close()

todo_router = APIRouter()

@todo_router.get('/',
response_model=List[TodoRead],
status_code=200,
description="List of all todo items")
def todos(db:Session=Depends(get_db),skip:int=0,limit:int=10):
  todos =  db.query(Todo).offset(skip).limit(limit).all()
  return todos

@todo_router.get('/{todoID}',
response_model=TodoInDb,
status_code=200,
description="Get a todo item")
def todo(todoID:int, db:Session= Depends(get_db)):
  # todo = todoID-1
  # return db[todo]
  todo_item = db.query(Todo).filter(Todo.id==todoID).first()
  if todo_item is None:
    raise HTTPException(status_code=404,detail=f'Todo item {todoID} does not exist.')
  return todo_item

@todo_router.post('/',
response_model=TodoInDb,
status_code=200,
description="Add a todo item")
def create_todo(todo:TodoCreate, db:Session = Depends(get_db)):
  # db.append(payload.dict())
  # return db[-1]
  todo_item = db.query(Todo).filter(Todo.title == todo.title).first()
  if todo_item:
    raise HTTPException(status_code=404,detail=f'Sorry {todo.title} already exist.')
  todo_item = Todo(**todo.dict())
  db.add(todo_item)
  db.commit()
  db.refresh(todo_item)
  return todo_item

@todo_router.put('/{todoID}',
response_model=Dict[str,str],
status_code=200,
description="Update a todo item")
def update_todo(todoID:int, todo:TodoPut, db:Session = Depends(get_db)):
  todo_item = db.query(Todo).filter(Todo.id == todoID).first()
  if todo_item is None:
    raise HTTPException(status_code=404,detail=f'Todo item {todoID} does not exist.')
  todo_item.title = todo.title
  todo_item.description = todo.description
  todo_item.completed = todo.completed
  db.commit()
  db.refresh(todo_item)
  return {'message':f'Todo item {todoID} is successfully updated.'}

@todo_router.delete('/{todoID}',
response_model=Dict[str,str],
status_code=200,
description="Delete a todo item")
def delete_todo(todoID:int, db:Session = Depends(get_db)):
  # db.pop(todoID-1)
  todo_item = db.query(Todo).filter(Todo.id == todoID).first()
  if todo_item is None:
    raise HTTPException(status_code=404,detail=f'Todo item {todoID} does not exist.')
  db.delete(todo_item)
  db.commit()
  return {'message':f'Todo item {todoID} is successfully deleted.'}


"""Dependency Injection (DI) is a way functions and classes declare things they need to work."""
"""In FastAPI context ,endpoint functions are called path operation functions."""
