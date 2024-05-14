from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.clinicalModel import ClinicalModel
from bson import ObjectId
from src.utils.dateFns import DateClass as eventYear


def get_collection_clinicals(request: Request):
    return request.app.database['clinical']


def create_clinical(request: Request, clinical: ClinicalModel = Body(...)):

    #dct.pop('vitals')
    #dct.pop('viralLoad')
    new_clinical = get_collection_clinicals(request).insert_one(jsonable_encoder(clinical))
    print(new_clinical)
    created_clinical = get_collection_clinicals(request).find_one({"_id": new_clinical.inserted_id})
    return created_clinical


def list_clinicals(request: Request, limit: int):
    users = list(get_collection_clinicals(request).find(limit=limit))
    return users


def find_clinical(request: Request, user_id: object):
    print("ID =========", id)
    if clinical := get_collection_clinicals(request).find({"user_id": user_id}).sort({'created_at': -1}):
        return clinical
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Clinical with id {id} not found!")


def delete_clinical(request: Request, id: str):
    deleted_clinical = get_collection_clinicals(request).delete_one({"_id": ObjectId(id)})
    if deleted_clinical.deleted_count == 1:
        return f"Clinical with id {id} deleted successfully"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Clinical with id {id} not found!")
