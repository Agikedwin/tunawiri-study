from fastapi import BackgroundTasks, Request, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.mHTreatmentGad7ScaleModel import MentalHealthGad7ScaleModel
from bson import ObjectId


def getcollection_mental_health_gad7Scale(request: Request):
    return request.app.database['mentalhealthGad7Scale']


def create_mental_health_gad7Scale(request: Request, mentalhealthGad7Scale: MentalHealthGad7ScaleModel = Body(...)):
    new_mental = getcollection_mental_health_gad7Scale(request).insert_one(jsonable_encoder(mentalhealthGad7Scale))
    return getcollection_mental_health_gad7Scale(request).find_one({"_id": new_mental.inserted_id})


def list_mental_health_gad7Scale(request: Request, limit: int):
    return list(getcollection_mental_health_gad7Scale(request).find(limit=limit))


def find_one_mental_health_gad7Scale(request: Request, user_id: object):
    if mental := getcollection_mental_health_gad7Scale(request).find_one({"user_id":user_id}):
        return mental
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Metal Health Gad7Scale with Id {id} not found")


def delete_menta_health_gad7Scale(request: Request, id: str):
    if getcollection_mental_health_gad7Scale(request).delete_one({"_id": ObjectId(id)}).deleted_count == 1:
        return f"Mental Health Gad7Scale  with id {id}  deleted successfully"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Mental Health Gad7Scale with id {id} not found")
