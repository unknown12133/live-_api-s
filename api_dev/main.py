# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class UserCreate(BaseModel):
#     name: str
#     email: str
#     age: int

# @app.get("/health")
# def health():
#     return {"message": "API is running"}

# @app.get("/users/{user_id}")
# def get_user(user_id: int,limit:int=10):
#     return {"id": user_id, "name": "Test User"}

# @app.post("/users")
# def create_user(user: UserCreate):
#     return {
#         "status": "created",
#         "user": user.name
#     }
# @app.post("/users/{user_id}")
# def update_user(user_id: int,user: dict):
#     return {
#         "id": user_id,
#         "status": "posted",
#         "user": user
#     }
    
# @app.get("/users")
# def get_users(limit: int = 10,age:int=1):
#     return {
#         "limit": limit,
#         "users": ["Alice", "Bob"]
#     }

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
from database import engine, SessionLocal
from schemas import UserCreate, UserResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    db_user = models.User(
        name=user.name,
        email=user.email
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

