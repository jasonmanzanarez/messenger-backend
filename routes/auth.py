from fastapi import APIRouter, HTTPException
from models.user import UserCreate, UserLogin
from database.mongo import users_collection
from passlib.hash import bcrypt
from jose import jwt
import os

auth_router = APIRouter(prefix="/auth", tags=["auth"])

SECRET_KEY = os.environ.get("SECRET_KEY", "supersecret123")

@auth_router.post("/register")
def register(user: UserCreate):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered.")
    
    hashed_pw = bcrypt.hash(user.password)
    users_collection.insert_one({
        "email": user.email,
        "username": user.username,
        "password": hashed_pw
    })
    return {"message": "User registered successfully."}

@auth_router.post("/login")
def login(user: UserLogin):
    db_user = users_collection.find_one({"email": user.email})
    if not db_user or not bcrypt.verify(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    
    token = jwt.encode({"sub": user.email}, SECRET_KEY, algorithm="HS256")
    return {"access_token": token}
