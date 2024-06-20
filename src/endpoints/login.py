from fastapi import APIRouter, Body, Request, status
from typing import List
from src.models.userModel import LoginModel

import src.rules.userRules as users
from bson import ObjectId

router = APIRouter(prefix="/login",
                   tags=["Login"])


@router.post("/")
def create_user(request: Request, login: LoginModel = Body(...)):
    response = users.authenticate_user(request, login)
    if response:
        return users.authenticate_user(request, login)
    else:
        None
