from fastapi import APIRouter, Body, Request, status
from typing import List
import src.rules.MentalHealthTreatmentRule as mTreatmentRule
from src.models.mHTreatmentAntenatalModel import GeneralTreatmentAntenatalModel

router = APIRouter(prefix="/antenatal", tags=["GeneralTreatmentAntenatal"])


@router.post('/', response_description='Create New Mental  Health Treatment', status_code=status.HTTP_201_CREATED,
             response_model=GeneralTreatmentAntenatalModel)
def create_mental_health_antenatal(request: Request, mentalHealth : GeneralTreatmentAntenatalModel = Body(...)):
    return mTreatmentRule.create_mentalHealth(request, mentalHealth)


@router.get("/", response_description="Get Mental  Health Treatment", response_model = List[GeneralTreatmentAntenatalModel])
def list_mental_health_antenatal(request: Request):
    return mTreatmentRule.list_mentalHealths(request, 1000)


@router.get("/{id}", response_description="Get a single Mental  Health Treatment by Id", response_model = List[GeneralTreatmentAntenatalModel])
def find_mental_health_antenatal(request: Request, id: str):
    return mTreatmentRule.find_mentalHealth(request, id)


@router.delete("/{id}", response_description="Delete Mental  Health Treatment ")
def delete_mental_health_antenatal(request: Request, id: str):
    return mTreatmentRule.delete_mentalHealth(request, id)
