from fastapi import APIRouter, Body, Request, status
from typing import List
from src.models.case_review_initial import CaseReviewInitialModel

import src.rules.caseReviewInitialRule as caseInitial

router = APIRouter(prefix="/caseInitial",
                   tags=["CaseInitial"])


@router.post("/", response_description="Create a new Case Initial", status_code=status.HTTP_201_CREATED,
             response_model=CaseReviewInitialModel)
def create_case_initial(request: Request, case_initial: CaseReviewInitialModel = Body(...)):
    return caseInitial.create_case_review(request, case_initial)


@router.get("/", response_description="List case_initial", response_model=List[CaseReviewInitialModel])
def list_case_initial(request: Request):
    return caseInitial.list_created_case_review(request, 10000)


@router.get("/{id}", response_description="Get a single caseInitial by id", response_model=List[CaseReviewInitialModel])
def find_caseInitial(request: Request, id: object):
    return caseInitial.find_case_review(request, id)


@router.delete("/{id}", response_description="Delete a caseInitial")
def delete_Clinical(request: Request, id: object):
    return caseInitial.delete_case_review(request, id)
