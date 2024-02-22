from fastapi import APIRouter, Body, Request, status
from typing import List
from src.models.userModel import User

import src.rules.userRules as users

router = APIRouter(prefix="/user",
    tags=["User"])

@router.post("/", response_description="Create a new user", status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(request: Request, user: User = Body(...)):  
    print(user)    
    return  await users.create_user(request,user)

@router.get("/", response_description="List users", response_model=List[User])
def list_users(request: Request):
    return users.list_users(request, 100)

@router.get("/{id}", response_description="Get a single user by id", response_model=User)
def find_user(request: Request, id: str):    
    return users.find_user(request, id)


@router.delete("/{id}", response_description="Delete a user")
def delete_user(request: Request, id:str):
    return users.delete_user(request, id)