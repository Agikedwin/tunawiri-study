from fastapi import APIRouter, Body, Request, status
from typing import List
from src.models.userModel import User, StaffModel

import src.rules.userRules as users
from typing import Any, Dict, List, Union
from fastapi.encoders import jsonable_encoder
import json

from bson import ObjectId

router = APIRouter(prefix="/user",
                   tags=["User","StaffModel"])


@router.post("/", response_description="Create a new user", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(request: Request, user: User = Body(...)):
    print(user)
    return users.create_user(request, user)


@router.get("/", response_description="List users", response_model=List[User])
def list_users(request: Request):
    return users.list_users(request, 10000)


@router.get("/{id}", response_description="Get a single user by id", response_model=User)
def find_user(request: Request, id: str):
    return users.find_user(request, id)


@router.delete("/{id}", response_description="Delete a user")
def delete_user(request: Request, id: str):
    return users.delete_user(request, id)


@router.get("/severity/{severity}")
def get_all_severity(request: Request, severity: object):

    return users.get_user_severities(request, severity)


#Staff begins here
@router.post("/staff", response_description="Create a new Staff", status_code=status.HTTP_201_CREATED, response_model=StaffModel)
def create_staff(request: Request, staff: StaffModel = Body(...)):
    return users.create_staff(request, staff)

@router.get("/user/staff", response_description="List Staff", response_model=List[StaffModel])
def list_staff(request: Request):
    print("Getting staff -------------------------------------")
    return users.list_staff(request, 10000)


@router.get("/staffnew", response_description="Get a single user by id", response_model=StaffModel)
def find_staff(request: Request, id: str):
    return users.find_staff(request, id)
