from fastapi import APIRouter, Body, Request, status
from typing import List
import src.rules.mHTreatmentGad7ScaleRules as gad7ScaleRule
from src.models.mHTreatmentGad7ScaleModel import MentalHealthGad7ScaleModel

router = APIRouter(prefix="/gad7Scale", tags=["MentalHealthGad7Scale"])


@router.post('/', response_description='Create New Mental Health Gad7Scale', status_code=status.HTTP_201_CREATED,
             response_model=MentalHealthGad7ScaleModel)
def create_mental_health_gad7Scale(request: Request, mentalHealth: MentalHealthGad7ScaleModel = Body(...)):
    return gad7ScaleRule.create_mental_health_gad7Scale(request, mentalHealth)


@router.get("/", response_description="Get Mental Health Gad7Scale", response_model=List[MentalHealthGad7ScaleModel])
def list_mental_health_gad7Scale(request: Request):
    return gad7ScaleRule.list_mental_health_gad7Scale(request, 1000)


@router.get("/{id}", response_description="Get a single Mental Health Gad7Scale by Id",
            response_model=MentalHealthGad7ScaleModel)
def find_mental_health_gad7Scale(request: Request, id: str):
    return gad7ScaleRule.find_one_mental_health_gad7Scale(request, id)


@router.delete("/{id}", response_description="Delete Mental Health Gad7Scale ")
def delete_mental_health_gad7Scale(request: Request, id: str):
    return gad7ScaleRule.delete_menta_health_gad7Scale(request, id)
