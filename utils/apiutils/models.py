from pydantic import BaseModel

class BrailleLang(BaseModel):
    id:int
    data:str

    class Config:
        orm_mode=True

class DBpost(BaseModel):
    id:str
    data:str

    class Config:
        orm_mode=True