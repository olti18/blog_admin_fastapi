import Backend.src.auth 
from fastapi import FastAPI ,HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from Backend.src.models.models import Base, User
from Backend.src.models.models import Base, User
from Backend.src.schemas import schemas
from Backend.src.auth import auth
from Backend.src.database.database import SessionLocal, engine
from sqlalchemy.orm import Session 
from typing import Annotated 
import Backend.src.auth
from Backend.src.models.models import Base, User
from datetime import timedelta

Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(auth.router)  # Include the auth router

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

















