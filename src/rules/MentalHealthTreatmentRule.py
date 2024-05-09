from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.mHTreatmentGeneralModel import GeneralTreatmentModel
from bson import ObjectId
from src.utils.dateFns import DateClass as eventYear


def get_collection_mentalHealths(request: Request):
    return request.app.database['mentalHealth']


def create_mentalHealth(request: Request, mentalHealth: GeneralTreatmentModel = Body(...)):

    new_mentalHealth = get_collection_mentalHealths(request).insert_one(jsonable_encoder(mentalHealth))
    print(new_mentalHealth)
    created_mentalHealth = get_collection_mentalHealths(request).find_one({"_id": new_mentalHealth.inserted_id})
    return created_mentalHealth


def list_mentalHealths(request: Request, limit: int):
    mentalHealth = list(get_collection_mentalHealths(request).find(limit=limit))
    return mentalHealth


def find_mentalHealth(request: Request, user_id: str):
    if mentalHealth := get_collection_mentalHealths(request).find_one({"user_id": user_id}):
        return mentalHealth
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"mentalHealth with id {id} not found!")


def delete_mentalHealth(request: Request, id: str):
    deleted_mentalHealth = get_collection_mentalHealths(request).delete_one({"_id": ObjectId(id)})
    if deleted_mentalHealth.deleted_count == 1:
        return f"mentalHealth with id {id} deleted successfully"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"mentalHealth with id {id} not found!")
