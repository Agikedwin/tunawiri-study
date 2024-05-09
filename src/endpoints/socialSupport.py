from fastapi import APIRouter, Body, Request, status
from typing import List
from src.models.socialsupport import SocialSupportModel

import src.rules.socialSupportRules as socialSupportRules

router = APIRouter(prefix="/socialsupport",
    tags=["Socialsupport"])

@router.post("/", response_description="Create a new socialsupport", status_code=status.HTTP_201_CREATED, response_model=SocialSupportModel)
def create_social_support(request: Request, socialsupport: SocialSupportModel = Body(...)):  
    print(socialsupport)    
    return  socialSupportRules.create_social_support(request,socialsupport)

@router.get("/", response_description="List Social Support Rules", response_model=List[SocialSupportModel])
def list_social_support(request: Request):
    return socialSupportRules.list_socialsupport(request, 1000)

@router.get("/{id}", response_description="Get a single Social Support Rules by id", response_model=SocialSupportModel)
def find_social_support(request: Request, id: str):    
    return socialSupportRules.find_socialsupport(request, id)


@router.delete("/{id}", response_description="Delete a Social Support Rules")
def delete_socialSupportRules(request: Request, id:str):
    return socialSupportRules.delete_socialsupport(request, id)