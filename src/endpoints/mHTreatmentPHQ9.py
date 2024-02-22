from fastapi import APIRouter, Body, Request, status
from typing import List
import src.rules.mHTreatmentPHQ9Rule as phq9Rule
from src.models.mHTreatmentPHQ9Model import MentalHealthPHQ9Model

router = APIRouter(prefix="/phq9", tags=["MentalHealthPhq9"])


@router.post('/', response_description='Create New Mental Health Phq9', status_code=status.HTTP_201_CREATED,
             response_model=MentalHealthPHQ9Model)
def create_mental_health_phq9(request: Request, mentalHealth: MentalHealthPHQ9Model = Body(...)):
    return phq9Rule.create_mental_health_phq9(request, mentalHealth)


@router.get("/", response_description="Get Mental Health Phq9", response_model=MentalHealthPHQ9Model)
def list_mental_health_phq9(request: Request):
    return phq9Rule.list_mental_health_phq9(request, 1000)


@router.get("/{id}", response_description="Get a single Mental Health Phq9 by Id", response_model=MentalHealthPHQ9Model)
def find_mental_health_phq9(request: Request, id: str):
    return phq9Rule.find_one_mental_health_phq9(request, id)


@router.delete("/{id}", response_description="Delete Mental Health Phq9 ")
def delete_mental_health_phq9(request: Request, id: str):
    return phq9Rule.delete_menta_health_phq9(request, id)
