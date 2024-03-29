from fastapi import BackgroundTasks, Request, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.mHTreatmentTraumaExposureModel import MentalHealthTraumaExposureModel
from bson import ObjectId


def getcollection_mental_health_traumaScale(request: Request):
    return request.app.database['mentalhealthTraumaScale']


def create_mental_health_traumaScale(request: Request, mentalhealthTraumaScale: MentalHealthTraumaExposureModel = Body(...)):
    new_mental = getcollection_mental_health_traumaScale(request).insert_one(jsonable_encoder(mentalhealthTraumaScale))
    return getcollection_mental_health_traumaScale(request).find_one({"_id": new_mental.inserted_id})


def list_mental_health_traumaScale(request: Request, limit: int):
    return list(getcollection_mental_health_traumaScale(request).find(limit=limit))


def find_one_mental_health_traumaScale(request: Request, id: str):
    if mental := getcollection_mental_health_traumaScale(request).find_one({"id": ObjectId(id)}):
        return mental
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Metal Health TraumaScale with Id {id} not found")


def delete_menta_health_traumaScale(request: Request, id: str):
    if getcollection_mental_health_traumaScale(request).delete_one({"_id": ObjectId(id)}).deleted_count == 1:
        return f"Mental Health TraumaScale  with id {id}  deleted successfully"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Mental Health TraumaScale with id {id} not found")
