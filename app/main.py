from contextlib import asynccontextmanager
from app import settings
from sqlalchemy import engine_from_config
from sqlmodel import SQLModel, Field, create_engine, Session,select

from fastapi import FastAPI


class ToDo(SQLModel, table=True):
    ID: int = Field(primary_key=True)
    Content : str

connection_string = str (settings.DATABASE_URL).replace ("postgresql", "postgresql" + "psycopg"
)
engine = create_engine(connection_string)

def create_tables():
    SQLModel.metadata.create_all(create_engine)

@asynccontextmanager
async def LahoreClass(app:FastAPI):
    print("Creating table..")
    create_tables()
    yield 
    

app = FastAPI(lifespan = LahoreClass )
# 
# 
# title="Hello World API with DB", 
#     version="0.0.1",
#     servers=[
#         {
#             "url": "http://0.0.0.0:8000", # ADD NGROK URL Here Before Creating GPT Action
#             "description": "Development Server"
#         }
#         ])

# def get_session():
#     with Session(engine) as session:
#         yield session


@app.get("/")
def read_root():
    return {"Hello": "World"}


# # 1. cREAT TODOS
# @app.post("/todos")
# def creat_todo(todo_contect:ToDo)
#     with Session(engine_from_config)as session:
#         session.add(todo_content)
#         session/commit()        
#         session.refresh(todo_contect)
#         return todo_contect



# 2. TODOS


