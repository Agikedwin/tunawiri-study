from fastapi import APIRouter, Body, Request, status
from typing import List
from src.models.case_review_follwup import CaseReviewFollowupModel

import src.rules.caseReviewFollowupRule as caseFollowup

router = APIRouter(prefix="/caseFollowup",
                   tags=["Case Followup"])


@router.post("/", response_description="Create a new Case Followup", status_code=status.HTTP_201_CREATED,
             response_model=CaseReviewFollowupModel)
def create_case_initial(request: Request, case_initial: CaseReviewFollowupModel = Body(...)):
    return caseFollowup.create_case_review(request, case_initial)


@router.get("/", response_description="List caseFollowup", response_model=List[CaseReviewFollowupModel])
def list_case_initial(request: Request):
    return caseFollowup.list_created_case_review(request, 10000)


@router.get("/{id}", response_description="Get a single caseFollowup by id", response_model=List[CaseReviewFollowupModel])
def find_caseInitial(request: Request, id: object):
    return caseFollowup.find_case_review(request, id)


@router.delete("/{id}", response_description="Delete a caseFollowup")
def delete_Clinical(request: Request, id: object):
    return caseFollowup.delete_case_review(request, id)
