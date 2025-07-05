from fastapi import FastAPI ,HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from Backend.src.models import models
from Backend.src.database.database import SessionLocal, engine 
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class PostBase(BaseModel):
    title: str
    content: str
    author_id: int

class UserBase(BaseModel):
    username: str
    email: str
    password: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]  # <-- FIXED

# @app.get("/")
# def read_root():
#     return {"message": "API is working"}

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.dict())  # <-- FIXED: remove .models
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

