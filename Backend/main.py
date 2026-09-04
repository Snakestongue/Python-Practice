from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

class Task(BaseModel): #template for what a task must include
    title:str
    completed: bool = False
@app.get("/") # get, gets data
def home():
    return{
        "message": "Welcome"
    }

@app.get("/tasks/{task_id}") #uses link right below
def task(task_id: int):
    for x in tasks:
        if x["id"] == task_id:
            return x
    raise HTTPException(status_code=404, detail="Task not found")

app.post("/tasks") # post, puts data
def make_task(task:Task): #just like x:int, 
    new_task = {
        "id":len(tasks)+1,
        "title": task.title,
        "completed" : task.completed
    }
    tasks.append(new_task)
    return(new_task)
tasks=[
    {
        "id": 1,
        "title": "Learn math",
        "completed": False
    },
    {
        "id": 2,
        "title":"Practice math",
        "completed":  True
    },
    {
        "id":3,
        "title":"Do math test",
        "completed": False
    }
]
#To run uvicorn main:app --reload