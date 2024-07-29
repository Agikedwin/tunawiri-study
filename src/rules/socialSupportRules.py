from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.socialsupport import SocialSupportModel
from bson import ObjectId
from src.utils.dateFns import DateClass as eventYear



def get_collection_socialsupport(request: Request):
    return request.app.database['socialsupport']

def create_social_support(request: Request, social: SocialSupportModel = Body(...)):
    #print(social)
    print('-------------------------')
    #print( jsonable_encoder(social))
    print('-------------------------')
   
    
    support = jsonable_encoder(social)
    new_sosial_support =  get_collection_socialsupport(request).insert_one(support)
    created_support =  get_collection_socialsupport(request).find_one({"_id": new_sosial_support.inserted_id})
    return created_support

def list_socialsupport(request: Request, limit: int):
    socialsupport = list(get_collection_socialsupport(request).find(limit = limit))
    return socialsupport


def find_socialsupport(request: Request, user_id: str):
    if (socialsupport := get_collection_socialsupport(request).find({"user_id": user_id}).sort({'created_at': -1})):
        return socialsupport
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Social Support with id {id} not found!")


def delete_socialsupport(request: Request, id: str):
    socialsupport = get_collection_socialsupport(request).delete_one({"_id": ObjectId(id)})

    if socialsupport.deleted_count == 1:
        return f"Social Support with id {id} deleted sucessfully"

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Social Support with id {id} not found!")

