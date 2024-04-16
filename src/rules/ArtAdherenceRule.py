from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.ArtAdherenceModel import ArtAdherenceModel
from bson import ObjectId
from src.utils.dateFns import DateClass as eventYear


def get_collection_arts(request: Request):
    return request.app.database['artAdherence']


def create_art(request: Request, art: ArtAdherenceModel = Body(...)):

    new_art = get_collection_arts(request).insert_one(jsonable_encoder(art))
    print(new_art)
    created_art = get_collection_arts(request).find_one({"_id": new_art.inserted_id})
    return created_art


def list_arts(request: Request, limit: int):
    art = list(get_collection_arts(request).find(limit=limit))
    return art


def find_art(request: Request, id: str):
    if art := get_collection_arts(request).find_one({"_id": ObjectId(id)}):
        return art
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"art with id {id} not found!")


def delete_art(request: Request, id: str):
    deleted_art = get_collection_arts(request).delete_one({"_id": ObjectId(id)})
    if deleted_art.deleted_count == 1:
        return f"art with id {id} deleted successfully"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"art with id {id} not found!")
