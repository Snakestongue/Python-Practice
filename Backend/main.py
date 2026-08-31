from fastapi import FastAPI, HTTPException
app = FastAPI()

@app.get("/")
def home():
    return{
        "message": "Welcome"
    }

@app.get("/tasks/{task_id}")
def task(task_id: int):
    for x in tasks:
        if x["id"] == task_id:
            return x
    raise HTTPException(status_code=404, detail="Task not found")
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