from fastapi import APIRouter, Body, Request, status
from typing import List
import src.rules.mHTreatmentAntenatalRules as antenatalRule
from src.models.mHTreatmentAntenatalModel import MentalHealthAntenatalModel

router = APIRouter(prefix="/antenatal", tags=["MentalHealthAntenatal"])


@router.post('/', response_description='Create New Mental Health Antenatal', status_code=status.HTTP_201_CREATED,
             response_model=MentalHealthAntenatalModel)
def create_mental_health_antenatal(request: Request, mentalHealth: MentalHealthAntenatalModel = Body(...)):
    return antenatalRule.create_mental_health_antenatal(request, mentalHealth)


@router.get("/", response_description="Get Mental Health Antenatal", response_model=List[MentalHealthAntenatalModel])
def list_mental_health_antenatal(request: Request):
    return antenatalRule.list_mental_health_antenatal(request, 1000)


@router.get("/{id}", response_description="Get a single Mental Health Antenatal by Id", response_model=List[MentalHealthAntenatalModel])
def find_mental_health_antenatal(request: Request, id: str):
    return antenatalRule.find_one_mental_health_antenatal(request, id)


@router.delete("/{id}", response_description="Delete Mental Health Antenatal ")
def delete_mental_health_antenatal(request: Request, id: str):
    return antenatalRule.delete_mental_health_antenatal(request, id)
