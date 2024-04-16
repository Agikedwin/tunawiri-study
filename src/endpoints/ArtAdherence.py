from fastapi import APIRouter, Body, Request, status
from typing import List
import src.rules.ArtAdherenceRule as artRule
from src.models.ArtAdherenceModel import ArtAdherenceModel

router = APIRouter(prefix="/artAdherence", tags=["ArtAdherence"])


@router.post('/', response_description='Create New Art Adherence', status_code=status.HTTP_201_CREATED,
             response_model=ArtAdherenceModel)
def create_mental_health_antenatal(request: Request, artAdherence: ArtAdherenceModel = Body(...)):
    return artRule.create_art(request, artAdherence)


@router.get("/", response_description="Get Art Adherence", response_model=ArtAdherenceModel)
def list_mental_health_antenatal(request: Request):
    return artRule.list_arts(request, 1000)


@router.get("/{id}", response_description="Get a single Art Adherence by Id", response_model=ArtAdherenceModel)
def find_mental_health_antenatal(request: Request, id: str):
    return artRule.find_art(request, id)


@router.delete("/{id}", response_description="Delete Art Adherence ")
def delete_mental_health_antenatal(request: Request, id: str):
    return artRule.delete_art(request, id)
