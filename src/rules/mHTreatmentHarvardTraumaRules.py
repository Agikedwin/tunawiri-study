from fastapi import BackgroundTasks, Request, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.mHTreatmentHarvardTraumaModel import MentalHealthHarvardTraumaModel
from bson import ObjectId


def getcollection_mental_health_harvardTrauma(request: Request):
    return request.app.database['mentalhealthHarvardTrauma']


def create_mental_health_harvardTrauma(request: Request, mentalhealthHarvardTrauma: MentalHealthHarvardTraumaModel = Body(...)):
    new_mental = getcollection_mental_health_harvardTrauma(request).insert_one(jsonable_encoder(mentalhealthHarvardTrauma))
    return getcollection_mental_health_harvardTrauma(request).find_one({"_id": new_mental.inserted_id})


def list_mental_health_harvardTrauma(request: Request, limit: int):
    return list(getcollection_mental_health_harvardTrauma(request).find(limit=limit))


def find_one_mental_health_harvardTrauma(request: Request, user_id: object):
    if mental := getcollection_mental_health_harvardTrauma(request).find({"user_id": user_id}).sort({'created_at': -1}):
        return mental
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Metal Health HarvardTrauma with Id {id} not found")


def delete_menta_health_harvardTrauma(request: Request, id: str):
    if getcollection_mental_health_harvardTrauma(request).delete_one({"_id": ObjectId(id)}).deleted_count == 1:
        return f"Mental Health HarvardTrauma  with id {id}  deleted successfully"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Mental Health HarvardTrauma with id {id} not found")
