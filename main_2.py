from fastapi import FastAPI
from app2.routers_dz import user, task

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)

#python3 -m uvicorn main_2:app