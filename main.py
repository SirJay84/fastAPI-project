from fastapi import FastAPI
from typing import Dict,List
from schemas import TodoCreate, TodoPut, Todo

app = FastAPI(
  title="Todo API",
  description="A Basic Todo API",
  version="0.1.0",
  docs_url="/developer/docs",
  redoc_url="/developer/redoc",
  contact={"name": "Jimmy","email":"jimbotela@icloud.com"}
)

db = []

@app.get('/',status_code=200,description="Home route")
def index():
  return {'message':'Hello Jimmy'}

@app.get('/todos',
tags=['TODOS'],
response_model=List[Todo],
status_code=200,
description="List of all todo items",
responses={200:{'description':'OK'}, 201:{'description':'Accepted'}})
def todos():
  return db

@app.get('/todos/{todoID}',
tags=['TODOS'],
response_model=Todo,
status_code=200,
description="Get a todo item",
responses={200:{'description':'OK'}, 201:{'description':'Accepted'}})
def todo(todoID:int):
  todo = todoID-1
  return db[todo]


@app.post('/todos',
tags=['TODOS'],
response_model=Todo,
status_code=200,
description="Add a todo item",
responses={200:{'description':'OK'}, 201:{'description':'Accepted'}})
def add_todo(payload:TodoCreate):
  db.append(payload.dict())
  return db[-1]
  

@app.put('/todos/{todoID}',
tags=['TODOS'],
response_model=Todo,
status_code=200,
description="Update a todo item",
responses={200:{'description':'OK'}, 201:{'description':'Accepted'}})
def update_todo(todoID:int):
  # todo = {id:None,'title':'Task 1', 'description':'Taking out Trash', 'completed':False, 'created':None}
  # todo.update({'completed':True})
  # db[0]['completed'] = True
  return {'message':'Todo item updated.'}

@app.delete('/todos/{todoID}',
tags=['TODOS'],
response_model=Dict[str,str],
status_code=200,
description="Delete a todo item",
responses={200:{'summary':'OK'}, 201:{'summary':'Accepted'}})
def delete_todo(todoID:int):
  db.pop(todoID-1)
  return {'message':'Todo item deleted.'}







