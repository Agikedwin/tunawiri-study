from fastapi import APIRouter, Body, Request, status
from typing import List
import src.rules.mHTreatmentSuicidalRules as suicidalRule
from src.models.mHTreatmentSuicidalModel import MentalHealthSuicidalModel

router = APIRouter(prefix="/suicidal", tags=["MentalHealthSuicidal"])


@router.post('/', response_description='Create New Mental Health Suicidal', status_code=status.HTTP_201_CREATED,
             response_model=MentalHealthSuicidalModel)
def create_mental_health_suicidal(request: Request, mentalHealth: MentalHealthSuicidalModel = Body(...)):
    return suicidalRule.create_mental_health_suicidal(request, mentalHealth)


@router.get("/", response_description="Get Mental Health Suicidal", response_model=List[MentalHealthSuicidalModel])
def list_mental_health_suicidal(request: Request):
    return suicidalRule.list_mental_health_suicidal(request, 1000)


@router.get("/{id}", response_description="Get a single Mental Health Suicidal by Id",
            response_model=MentalHealthSuicidalModel)
def find_mental_health_suicidal(request: Request, id: str):
    return suicidalRule.find_one_mental_health_suicidal(request, id)


@router.delete("/{id}", response_description="Delete Mental Health Suicidal ")
def delete_mental_health_suicidal(request: Request, id: str):
    return suicidalRule.delete_menta_health_suicidal(request, id)
