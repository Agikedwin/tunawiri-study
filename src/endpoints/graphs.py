from fastapi import APIRouter, Body, Request, status
from typing import List
from src.models.graphModels import VLgraphModel

import src.rules.clinicalRules as graphClinical

from src.models.graphModels import Gad7Model,PHQ9Model,Phq9Gad7

import src.rules.clinicalRules as graphClinical

import src.rules.mHTreatmentPHQ9Rule as phq9
import src.rules.mHTreatmentGad7ScaleRules as gad7

router = APIRouter(prefix="/graph",
                   tags=["Graphs"])



@router.get("/vl/{id}", response_description="Get a single Clinical by id", response_model=object)
def find_Clinical(request: Request, id: object):
    print("========================")
    return graphClinical.find_clinical_vl(request, id)

@router.get("/phq9/{id}", response_description="Get a single Clinical by id", response_model=object)
def find_Clinical(request: Request, id: object):
    print("========================")
    return phq9.find_one_mental_health_phq9(request, id)

@router.get("/gad7/{id}", response_description="Get a single Clinical by id", response_model=object)
def find_Clinical(request: Request, id: object):
    print("========================")
    gad7.find_one_mental_health_gad7Scale(request, id)

@router.get('phq9Gad7', response_description="Get all graph data", response_model=object)
def find_phq9_gad7(request: Request, user_id: object):
     return   phq9.find_phq9_gad7_graph(request, user_id)
