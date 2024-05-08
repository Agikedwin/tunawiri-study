from fastapi import APIRouter, Body, Request, status
from typing import List
import src.rules.mHTreatmentPostnatalRules as postnatalRule
from src.models.mHTreatmentPostnatalModel import MentalHealthPostnatalModel

router = APIRouter(prefix="/postnatal", tags=["MentalHealthPostnatal"])


@router.post('/', response_description='Create New Mental Health Postnatal', status_code=status.HTTP_201_CREATED,
             response_model=MentalHealthPostnatalModel)
def create_mental_health_postnatal(request: Request, mentalHealth: MentalHealthPostnatalModel = Body(...)):
    return postnatalRule.create_mental_health_postnatal(request, mentalHealth)


@router.get("/", response_description="Get Mental Health Postnatal", response_model=List[MentalHealthPostnatalModel])
def list_mental_health_postnatal(request: Request):
    return postnatalRule.list_mental_health_postnatal(request, 1000)


@router.get("/{id}", response_description="Get a single Mental Health Postnatal by Id", response_model=MentalHealthPostnatalModel)
def find_mental_health_postnatal(request: Request, id: str):
    return postnatalRule.find_one_mental_health_postnatal(request, id)


@router.delete("/{id}", response_description="Delete Mental Health Postnatal ")
def delete_mental_health_postnatal(request: Request, id: str):
    return postnatalRule.delete_menta_health_postnatal(request, id)
