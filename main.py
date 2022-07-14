from fastapi import FastAPI
from pydantic import BaseModel
import sqlalchemy
import databases
# import os

# DATABASE_URL = os.environ.get('postgresql://ugnlqudyvozqly:4d99c0cedc5a9dc2981f03252e471c33a97d9f8acdbedf4f93daeb27b44e013a@ec2-23-23-182-238.compute-1.amazonaws.com:5432/dbp5bm3o21pc8a')

DATABASE_URL = "postgresql://ugnlqudyvozqly:4d99c0cedc5a9dc2981f03252e471c33a97d9f8acdbedf4f93daeb27b44e013a@ec2-23-23-182-238.compute-1.amazonaws.com:5432/dbp5bm3o21pc8a"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

people_data = sqlalchemy.Table(
    "participants",
    metadata,
    sqlalchemy.Column("phone", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String),
    sqlalchemy.Column("college", sqlalchemy.String),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)


# class NoteIn(BaseModel):
#     text: str
#     completed: bool


# class Note(BaseModel):
#     id: int
#     text: str
#     completed: bool

class ppl(BaseModel):
    name: str
    phone: str
    college: str
    email: str
    name = phone = college = email = ""


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/signup/")
async def signup(details:ppl):
    query = people_data.insert().values(phone=details.phone,name=details.name,email=details.email,college=details.college)
    await database.execute(query)
    return {"Status":True}

@app.get("/")
def wel():
    return "Hello"

# uvicorn.run(app)