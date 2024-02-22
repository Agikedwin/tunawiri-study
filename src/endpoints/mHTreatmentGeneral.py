from fastapi import APIRouter, Body, Request, status
from typing import List
import src.rules.mHTreatmentGeneralRules as mentalRule
from src.models.mHTreatmentGeneralModel import MentalHealthTreatmentModel

router = APIRouter(prefix="/mentalhealth", tags=["MentalHealth"])


@router.post('/', response_description='Create New Mental Health', status_code=status.HTTP_201_CREATED,
             response_model=MentalHealthTreatmentModel)
def create_mental_health(request: Request, mentalHealth: MentalHealthTreatmentModel = Body(...)):
    return mentalRule.create_mental_health(request, mentalHealth)


@router.get("/", response_description="Get Mental Health", response_model=MentalHealthTreatmentModel)
def list_mental_health(request: Request):
    return mentalRule.list_mental_health(request, 1000)


@router.get("/{id}", response_description="Get a single mental Health by Id", response_model=MentalHealthTreatmentModel)
def find_mental_health(request: Request, id: str):
    return mentalRule.find_one_mental_health(request, id)


@router.delete("/{id}", response_description="Delete Mental Health ")
def delete_mental_health(request: Request, id: str):
    return mentalRule.delete_menta_health(request, id)
