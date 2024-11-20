from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.case_review_follwup import  CaseReviewFollowupModel
from bson import ObjectId

def get_collection_case_review(request: Request):
    return request.app.database['case_review_followup']


def create_case_review(request: Request, case_review: CaseReviewFollowupModel = Body(...)):

    #dct.pop('vitals')
    #dct.pop('viralLoad')
    new_case_review = get_collection_case_review(request).insert_one(jsonable_encoder(case_review))
    print(case_review)
    created_case_review = get_collection_case_review(request).find_one({"_id": new_case_review.inserted_id})
    return created_case_review


def list_created_case_review(request: Request, limit: int):
    case_review = list(get_collection_case_review(request).find(limit=limit))
    return case_review


def find_case_review(request: Request, user_id: object):
    print("ID =========", id)
    if clinical := get_collection_case_review(request).find({"user_id": user_id}).sort({'created_at': -1}):
        return clinical
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"created_case_review with id {id} not found!")


def delete_case_review(request: Request, id: str):
    deleted_case_review = get_collection_case_review(request).delete_one({"_id": ObjectId(id)})
    if deleted_case_review.deleted_count == 1:
        return f"created_case_review with id {id} deleted successfully"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"created_case_review with id {id} not found!")
