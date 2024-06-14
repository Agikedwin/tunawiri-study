from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.mHTreatmentModel import MmTreatmentModelModel
from bson import ObjectId
from src.utils.dateFns import DateClass as eventYear


def get_collection_treatments(request: Request):
    return request.app.database['treatmentTreatment']


def create_treatment(request: Request, treatment: MmTreatmentModelModel = Body(...)):

    new_treatment = get_collection_treatments(request).insert_one(jsonable_encoder(treatment))
    print(new_treatment)
    created_treatment = get_collection_treatments(request).find_one({"_id": new_treatment.inserted_id})
    return created_treatment


def list_treatments(request: Request, limit: int):
    treatment = list(get_collection_treatments(request).find(limit=limit))
    return treatment


def find_treatment(request: Request, user_id: object):
    if treatment := get_collection_treatments(request).find({"user_id": user_id}).sort({'created_at': -1}):
        return treatment
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"treatment with id {user_id} not found!")


def delete_treatment(request: Request, iuser_id: object):
    deleted_treatment = get_collection_treatments(request).delete_one({"_id": ObjectId(iuser_id)})
    if deleted_treatment.deleted_count == 1:
        return f"treatment with id {id} deleted successfully"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"treatment with id {iuser_id} not found!")
