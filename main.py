import json
from unicodedata import name
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

class ppl(BaseModel):
    name: str
    phone: str
    college: str
    email: str
    name = phone = college = email = ""

app = FastAPI()

@app.post("/signup/")
def signup(details:ppl):
    return details.name

@app.get("/")
def wel():
    return "Hello"

# uvicorn.run(app)