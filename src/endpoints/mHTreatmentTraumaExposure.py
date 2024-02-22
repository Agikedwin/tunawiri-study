from fastapi import APIRouter, Body, Request, status
from typing import List
import src.rules.mHTreatmentTraumaExposureRules as traumaScaleRule
from src.models.mHTreatmentTraumaExposureModel import MentalHealthTraumaExposureModel

router = APIRouter(prefix="/traumaScale", tags=["MentalHealthTraumaScale"])


@router.post('/', response_description='Create New Mental Health TraumaScale', status_code=status.HTTP_201_CREATED,
             response_model=MentalHealthTraumaExposureModel)
def create_mental_health_traumaScale(request: Request, mentalHealth: MentalHealthTraumaExposureModel = Body(...)):
    return traumaScaleRule.create_mental_health_traumaScale(request, mentalHealth)


@router.get("/", response_description="Get Mental Health TraumaScale", response_model=MentalHealthTraumaExposureModel)
def list_mental_health_traumaScale(request: Request):
    return traumaScaleRule.list_mental_health_traumaScale(request, 1000)


@router.get("/{id}", response_description="Get a single Mental Health TraumaScale by Id",
            response_model=MentalHealthTraumaExposureModel)
def find_mental_health_traumaScale(request: Request, id: str):
    return traumaScaleRule.find_one_mental_health_traumaScale(request, id)


@router.delete("/{id}", response_description="Delete Mental Health TraumaScale ")
def delete_mental_health_traumaScale(request: Request, id: str):
    return traumaScaleRule.delete_menta_health_traumaScale(request, id)
