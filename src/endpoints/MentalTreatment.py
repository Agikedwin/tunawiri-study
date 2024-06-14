from fastapi import APIRouter, Body, Request, status
from typing import List
import src.rules.MentalTreatmentRule as mentalRule
from src.models.mHTreatmentModel import MmTreatmentModelModel

router = APIRouter(prefix="/mental", tags=["MentalTreatment"])


@router.post('/', response_description='Create New Treatment', status_code=status.HTTP_201_CREATED,
             response_model=MmTreatmentModelModel)
def create_mental_health_antenatal(request: Request, mentalHealth: MmTreatmentModelModel = Body(...)):
    return mentalRule.create_treatment(request, mentalHealth)


@router.get("/", response_description="Get Treatment", response_model=MmTreatmentModelModel)
def list_mental_health_antenatal(request: Request):
    return mentalRule.list_treatments(request, 1000)


@router.get("/{id}", response_description="Get a single Treatment by Id", response_model=List[MmTreatmentModelModel])
def find_mental_health_antenatal(request: Request, id: str):
    return mentalRule.find_treatment(request, id)


@router.delete("/{id}", response_description="Delete Treatment ")
def delete_mental_health_antenatal(request: Request, id: str):
    return mentalRule.delete_treatment(request, id)
