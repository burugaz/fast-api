from fastapi import FastAPI
from pydantic import BaseModel
from models import User

app = FastAPI()

class Numbers(BaseModel):
    num1: float
    num2: float

user = User(name="Дементьев Андрей", id=1)

@app.post("/calculate")
async def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}

@app.get("/users")
async def get_user():
    return user