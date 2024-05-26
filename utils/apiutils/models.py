from pydantic import BaseModel
from typing import List
from dataclasses import dataclass

@dataclass
class BrailleLang(BaseModel):
    data:str

    class Config:
        orm_mode=True

@dataclass
class DBpost(BaseModel):
    id:str
    time:str
    data:str

    class Config:
        orm_mode=True

@dataclass
class FullSensorData(BaseModel):
    time:str
    pos:str
    reference:List[float]
    finger1:List[float]
    finger2:List[float]
    finger3:List[float]

    class Config:
        orm_mode=True