import pydantic
from fastapi import FastAPI, Request
app = FastAPI(docs_url='/')


@app.get('/info')
async def info():
    return "Hello"

@app.post('/add')
async def add(name: str, age: int):
    print(name, age)
    return "Отправлено"

class User(pydantic.BaseModel):
    name: str
    age: int

