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

@app.get("/tasks/{task_id}") #uses link right below, gets 1 task
def task(task_id: int):
    for x in tasks:
        if x["id"] == task_id:
            return x
    raise HTTPException(status_code=404, detail="Task not found")

@app.get("/tasks")
def tasks_all(): #returns all tasks not just 1
    return tasks

app.post("/tasks") # post, puts data
def make_task(task:Task): #just like x:int, 
    new_task = {
        "id":len(tasks)+1,
        "title": task.title,
        "completed" : task.completed
    }
    tasks.append(new_task)
    return(new_task)

@app.delete("/tasks/{task_id}") #removes task
def remove_task(task_id: int):
    for x in tasks:
        if x["id"] == task_id:
            tasks.remove(x)
            return x
    raise HTTPException(status_code=404, detail="Task not found")

app.put("/tasks/{task_id}") # change WHOLE task, patch only part of it
def update(task_id: int, task: Task):
    for x in tasks:
        if x["id"]==task_id:
            x["title"] = task.title
            x["completed"] = task.completed
            return x
    raise HTTPException(status_code=404, detail="Task not found")

#filter/query
@app.get("/tasks")
def get_tasks(completed:bool=None): # none makes it optionals
    if completed == None:
        return tasks
    complete = []
    for x in tasks:
        if x["completed"]==completed:
            complete.append(x)
    return complete
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