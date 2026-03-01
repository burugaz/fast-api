from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from models import User, UserWithAge, Feedback

app = FastAPI()

# №1.1
@app.get("/")
async def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}


# №1.2
@app.get("/")
async def get_index():
    return FileResponse("index.html")


# №1.3
class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/calculate")
async def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}


# №1.4
user = User(name="Дементьев Андрей", id=1)

@app.get("/users")
async def get_user():
    return user


# №1.5
@app.post("/user")
async def check_adult(user: UserWithAge):
    is_adult = user.age >= 18

    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }

# №2.1
feedbacks = []

@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    feedbacks.append(feedback)

    return {
        "message": f"Feedback received. Thank you, {feedback.name}."
    }