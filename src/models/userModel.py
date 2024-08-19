import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, validator


class User(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    mch_number: str
    ccc_number: str | None = None
    ptid_number: str | None = None
    registration_level: str | None = None
    first_name: str
    other_names: str
    dob: str
    marital_status: str
    education_level: str
    reading_ability: str
    religion: str
    home_language: str
    study_id: str
    username: str | None = None
    user_role: str | None = None
    password: str | None = None
    fieldExists: bool | None = None

    created_at: datetime = datetime.now()


class TokenModel(BaseModel):
    access_token: str
    token_type: str


class LoginModel(BaseModel):
    username: str | None = None
    password: str | None = None

class StaffModel(BaseModel):
    job_title: str
    department: str
    phone_number: str
    first_name: str
    other_names: str
    date_of_reg: str
    registration_level: str
    facility_level: str
    staff_number: str
    permissions: object
    username: str | None = None
    user_role: str | None = None
    password: str | None = None
    field_exists: bool | None = None

