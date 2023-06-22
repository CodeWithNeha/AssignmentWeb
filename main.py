from fastapi import FastAPI,Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Dict
from migration import db
from constantstrings import *


app = FastAPI()
security = HTTPBasic()
# Task Model
class TASK(BaseModel):
    title: str
    description: str

# Authenticate User basic 
def authenticate(credentials: HTTPBasicCredentials):
    # For simplicity, I'll use a hardcoded username and password
    valid_username = "admin"
    valid_password = "password"

    if credentials.username != valid_username or credentials.password != valid_password:
        raise HTTPException(status_code=401, detail=CONSTANT_STRINGS.INVALID_CREDENTIAl)

# Get all tasks
@app.get("/tasks")
def get_tasks(): 
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tasks")
    result = cursor.fetchall()
    tasks = [{CONSTANT_STRINGS.ID: row[0], CONSTANT_STRINGS.TITLE: row[1], CONSTANT_STRINGS.DESCRIPTION: row[2]} for row in result]
    return tasks

# Get a single task by ID
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    result = cursor.fetchone()

    if result is None:
        raise HTTPException(status_code=404, detail=CONSTANT_STRINGS.TASK_NOT_FOUND)

    task = {CONSTANT_STRINGS.ID: result[0], CONSTANT_STRINGS.TITLE: result[1], CONSTANT_STRINGS.DESCRIPTION: result[2]}
    return task

# Create a new task
@app.post("/tasks")
def create_task(task: TASK,credentials: HTTPBasicCredentials = Depends(security)):
    authenticate(credentials)
    cursor = db.cursor()
    cursor.execute("INSERT INTO tasks (title, description) VALUES (%s, %s)", (task.title, task.description))
    db.commit()

    return {CONSTANT_STRINGS.MSG:CONSTANT_STRINGS.TASK_CREATED}

# Update an existing task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TASK, credentials: HTTPBasicCredentials = Depends(security)):
    authenticate(credentials)

    cursor = db.cursor()
    cursor.execute("UPDATE tasks SET title = %s, description = %s WHERE id = %s", (task.title, task.description, task_id))
    db.commit()

    return {CONSTANT_STRINGS.MSG: CONSTANT_STRINGS.TASk_UPDATED}

# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, credentials: HTTPBasicCredentials = Depends(security)):
    authenticate(credentials)

    cursor = db.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    db.commit()

    return {CONSTANT_STRINGS.MSG: CONSTANT_STRINGS.TASK_DELETED}


