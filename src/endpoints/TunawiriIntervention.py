from fastapi import APIRouter, Body, Request, status
from typing import List
import src.rules.TunawiriInterventionRule as interventionRule
from src.models.TunawiriInterventionModel import TunawiriInterventionModel

router = APIRouter(prefix="/interventions", tags=["MentalHealthInterventions"])


@router.post('/', response_description='Create New Mental Health Antenatal', status_code=status.HTTP_201_CREATED,
             response_model=TunawiriInterventionModel)
def create_mental_health_antenatal(request: Request, mentalHealth: TunawiriInterventionModel = Body(...)):
    print("=====================================")
    return interventionRule.create_intervention(request, mentalHealth)


@router.get("/", response_description="Get Mental Health Antenatal", response_model=TunawiriInterventionModel)
def list_mental_health_antenatal(request: Request):
    return interventionRule.list_interventions(request, 1000)


@router.get("/{id}", response_description="Get a single Mental Health Antenatal by Id", response_model=List[TunawiriInterventionModel])
def find_mental_health_antenatal(request: Request, id: str):
    return interventionRule.find_intervention(request, id)


@router.delete("/{id}", response_description="Delete Mental Health Antenatal ")
def delete_mental_health_antenatal(request: Request, id: str):
    return interventionRule.delete_intervention(request, id)
