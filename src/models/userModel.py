import uuid
from typing import Optional
from pydantic import BaseModel, Field, validator


class User(BaseModel):
    id: object = Field(default_factory=uuid.uuid4, alias='_id')
    mchNumber: int
    firstName: str
    otherNames: str
    age: int = Field(gt=0)
    maritalStatus: str
    educationLevel: str
    readingAbility: str
    religion: str
    homeLanguage: str
    householdSize: int
    pregnancyCount: int
    parity: int
    livingChildrenCount: int
    birthControlMethods: str
    pregnancyFeelings: str
    prePregnancyState: str
    partnerFeelings: str
    # username: Optional[str]
    # password: Optional[str]
    gender:  Optional[str]

    # @validator('gender')
    # def gender_must_be_male_or_femal(cls,gender):
    #     gen = ['Male','Female']
    #     if gender not in gen:
    #         raise validator(f'Gender must be in {gen}')
    #     return  gender
    # """ class Config:
    #     allow_population_by_filed_name =True
    #     schema_extra ={
    #         'example':{
    #             'first_name': 'agik',
    #             'other_names': 'edwin',
    #             'age': 30,
    #             'username':'agik123',
    #             'password':'agik1234',
    #             'gender': 'Male'
    #                     }
    #                 } """