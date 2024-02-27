from fastapi import APIRouter, Body, Request, status
from typing import List
from src.models.userModel import User

import src.rules.userRules as users

router = APIRouter(prefix="/home", tags=["Home"])

@router.get("/", response_description="Home Page", status_code=status.HTTP_201_CREATED)
def homePage():
    return  ' TUNAWIRI APP STARTED AND RUNNING'
