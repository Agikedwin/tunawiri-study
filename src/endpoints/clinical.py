from fastapi import APIRouter, Body, Request, status
from typing import List
from src.models.clinicalModel import ClinicalModel

import src.rules.clinicalRules as clinicals

router = APIRouter(prefix="/clinical",
                   tags=["Clinical"])


@router.post("/", response_description="Create a new Clinical", status_code=status.HTTP_201_CREATED,
             response_model=ClinicalModel)
def create_clinical(request: Request, clinical: ClinicalModel = Body(...)):
    return clinicals.create_clinical(request, clinical)


@router.get("/", response_description="List Clinicals", response_model=List[ClinicalModel])
def list_clinicals(request: Request):
    return clinicals.list_clinicals(request, 1000)


@router.get("/{id}", response_description="Get a single Clinical by id", response_model=ClinicalModel)
def find_Clinical(request: Request, id: str):
    return clinicals.find_clinical(request, id)


@router.delete("/{id}", response_description="Delete a Clinical")
def delete_Clinical(request: Request, id: str):
    return clinicals.delete_clinical(request, id)
