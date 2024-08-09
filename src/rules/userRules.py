from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.userModel import User
from bson import ObjectId
from src.utils.dateFns import DateClass as eventYear
from src.rules.loginRules import *


def get_collection_users(request: Request):
    return request.app.database['users']


def create_user(request: Request, user: User = Body(...)):
    try:
        user.username = user.mch_number
        user.password = get_password_hash(user.mch_number)
        user.user_role = 'user'
        user_id = user.mch_number
        ccc_number = user.ccc_number

        print("User ***",user_id)
        user = jsonable_encoder(user)
        #mchExixts = get_collection_users(request).find_one({'mch_number': user_id, 'ccc_number': ccc_number })

        mchExixts = get_collection_users(request).find_one({'$or': [{'mch_number': user_id},{'ccc_number': ccc_number}]})

        print(mchExixts)
        if mchExixts:
            user['fieldExists'] = True
            print("user already exists :::::: ", user)
            return user

        else:
            new_user = get_collection_users(request).insert_one(user)
            created_user = get_collection_users(request).find_one({"_id": new_user.inserted_id})
            return created_user

    except Exception:
        print("some error s")




def list_users(request: Request, limit: int):
    users = list(get_collection_users(request).find(limit=limit))
    return users


def find_user(request: Request, id: str):
    if user := get_collection_users(request).find_one({"_id": id}):
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found!")


def get_user_by_username(request: Request, username):
    return get_collection_users(request).find_one({"username": username})


def authenticate_user(request: Request, login):
    user = get_user_by_username(request, login.username)
    print("++++++++++++++++", login)

    if user is None:
        return {'data': 'Not found'}
    if user is not None:
        print(user['password'])
        print(login.password)
        #Validate password here
        is_password_valid = verify_password(login.password, user['password'])
        if is_password_valid:
            token = create_access_token({'username': user['username']})
            return {'token': token, 'message': 'success'}
        else:
            return {'token': None, 'message': 'failed'}


def delete_user(request: Request, id: str):
    deleted_user = get_collection_users(request).delete_one({"_id": ObjectId(id)})

    if deleted_user.deleted_count == 1:
        return f"User with id {id} deleted successfully"

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found!")


#Severity starts here

def get_collection_severity(request: Request, severity_list):
    print(severity_list[0])
    return request.app.database[severity_list[0]]


def get_user_severities(request: Request, severity_dict):
    severity_list = severity_dict.split(',')
    print('Severity ::: ', severity_list)
    user_id = set()

    # Get users with severity and remove duplicates
    for doc in list(get_collection_severity(request, severity_list).find({'severity': severity_list[1]})):
        user_id.add(doc['user_id'])

    # Get list of users
    severity_users = find_severity_users(request, list(user_id))
    return list(severity_users)


def find_severity_users(request: Request, id_list):
    print(id_list)
    users = list(get_collection_users(request).find({'_id': {'$in': id_list}}))
    print(users)
    return users
