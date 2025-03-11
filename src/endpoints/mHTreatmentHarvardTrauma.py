from fastapi import APIRouter, Body, Request, status
from typing import List
import src.rules.mHTreatmentHarvardTraumaRules as harvardTraumaRule
from src.models.mHTreatmentPTSDSymptomsModel import MentalHealthPTSDSymptomsModel

router = APIRouter(prefix="/ptsdsymptoms", tags=["MentalHealthPTSDSymptomsModel"])


@router.post('/', response_description='Create New Mental Health HarvardTrauma', status_code=status.HTTP_201_CREATED,
             response_model=MentalHealthPTSDSymptomsModel)
def create_mental_health_harvardTrauma(request: Request, mentalHealth: MentalHealthPTSDSymptomsModel = Body(...)):
    return harvardTraumaRule.create_mental_health_harvardTrauma(request, mentalHealth)


@router.get("/", response_description="Get Mental Health HarvardTrauma", response_model=List[MentalHealthPTSDSymptomsModel])
def list_mental_health_harvardTrauma(request: Request):
    return harvardTraumaRule.list_mental_health_harvardTrauma(request, 1000)


@router.get("/{id}", response_description="Get a single Mental Health HarvardTrauma by Id",
            response_model=List[MentalHealthPTSDSymptomsModel])
def find_mental_health_harvardTrauma(request: Request, id: str):
    return harvardTraumaRule.find_one_mental_health_harvardTrauma(request, id)


@router.delete("/{id}", response_description="Delete Mental Health HarvardTrauma ")
def delete_mental_health_harvardTrauma(request: Request, id: str):
    return harvardTraumaRule.delete_menta_health_harvardTrauma(request, id)
