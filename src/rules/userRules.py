from itertools import count

from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.userModel import User
from bson import ObjectId
from src.utils.dateFns import DateClass as eventYear
from src.rules.loginRules import *
from datetime import date


from  src.utils import  dateFns
now = datetime.now()

def get_collection_users(request: Request):
    return request.app.database['users']

def get_collection_staff(request: Request):
    return request.app.database['staff']


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

    count = 0

    for f in users:
        dob =  now.year - datetime.strptime(f['dob'], "%Y-%m-%dT%H:%M:%S.%fZ").year
        users[count]['dob'] = str(dob)
        count += 1
    return users


def find_user(request: Request, id: str):
    if user := get_collection_users(request).find_one({"_id": id}):
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found!")


def get_user_by_username(request: Request, username):
    return get_collection_users(request).find_one({"username": username})


def authenticate_user(request: Request, login):
    user = get_user_by_username(request, login.username)
    print(user,"++++++++++++++++", login)

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

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id ----- {id} not found!")


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


#Staff begins here
def create_staff(request, staff):
    try:

        staff.username = staff.staff_number
        staff.password = get_password_hash(staff.staff_number)
        staff.user_role = 'Staff'
        staff_number = staff.staff_number
        phone_number = staff.phone_number

        print("staff ***", staff_number)
        staff = jsonable_encoder(staff)
        # mchExixts = get_collection_users(request).find_one({'mch_number': user_id, 'ccc_number': ccc_number })



        staffNoExixts = get_collection_staff(request).find_one(
            {'$or': [{'staff_number': staff_number}, {'phone_number': phone_number}]})

        if staffNoExixts:
            staff['field_exists'] = True
            print("staff already exists :::::: ", staff)
            return staff

        else:
            new_staff = get_collection_staff(request).insert_one(staff)

            created_staff = get_collection_staff(request).find_one({"_id": new_staff.inserted_id})
            return created_staff

    except Exception:
        print("some error staff")


def list_staff(request: Request, limit: int):
    staff = list(get_collection_staff(request).find(limit=limit))
    print(staff)

    count = 0

    for f in staff:
        dob = datetime.strptime(f['date_of_reg'], "%Y-%m-%dT%H:%M:%S.%fZ").date()
        staff[count]['date_of_reg'] = str(dob)
        count += 1

    return staff


def find_staff(request: Request, id: str):
    if staff := get_collection_staff(request).find_one({"_id": id}):
        return staff
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"staff with  here id {id} not found!")


def get_staff_by_username(request: Request, username):
    return get_collection_staff(request).find_one({"username": username})


def authenticate_user(request: Request, login):
    staff = get_staff_by_username(request, login.username)
    print(staff,"++++++++++++++++", login)

    if staff is None:
        return {'data': 'Not found'}
    if staff is not None:
        print(staff['password'])
        print(login.password)
        #Validate password here
        is_password_valid = verify_password(login.password, staff['password'])
        if is_password_valid:
            token = create_access_token({'username': staff['username']})
            return {'token': token, 'message': 'success'}
        else:
            return {'token': None, 'message': 'failed'}

