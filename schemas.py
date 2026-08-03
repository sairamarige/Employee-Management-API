from pydantic import BaseModel
from typing import Literal,Optional

Role=Literal("intern","dev","manager")

class EmployeeCreate(BaseModel):
    name:str
    age:int
    department:str
    email:str

class EmployeeUpdate(BaseModel):
    """ Used for PATCH every field optional so only sent fields get changed"""
    name:Optional[str]=None,
    age:Optional[int]=None,
    department:Optional[str]=None,
    email:Optional[str]=None

class EmployeeResponse(EmployeeCreate):
    id:int
    model_config={

        "from attribute":True
    }

class Usercreate(BaseModel):
    username:str
    password:str
    email:str
    role:Role = "intern"

class Userlogin(BaseModel):
    email:str
    password:str

class UserResonse(BaseModel):
    id:int
    username:str
    email:str
    role:Role

    model_config={
        "from attribute":True
    }










