from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.TunawiriInterventionModel import TunawiriInterventionModel
from bson import ObjectId
from src.utils.dateFns import DateClass as eventYear


def get_collection_interventions(request: Request):
    return request.app.database['interventionTreatment']


def create_intervention(request: Request, intervention: TunawiriInterventionModel = Body(...)):

    new_intervention = get_collection_interventions(request).insert_one(jsonable_encoder(intervention))
    print(new_intervention)
    created_intervention = get_collection_interventions(request).find_one({"_id": new_intervention.inserted_id})
    return created_intervention


def list_interventions(request: Request, limit: int):
    intervention = list(get_collection_interventions(request).find(limit=limit))
    return intervention


def find_intervention(request: Request, user_id: object):
    if intervention := get_collection_interventions(request).find({"user_id": user_id}).sort({'created_at': -1}):
        return intervention
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"intervention with id {user_id} not found!")


def delete_intervention(request: Request, user_id: object):
    deleted_intervention = get_collection_interventions(request).delete_one({"_id": ObjectId(user_id)})
    if deleted_intervention.deleted_count == 1:
        return f"intervention with id {id} deleted successfully"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"intervention with id {user_id} not found!")
