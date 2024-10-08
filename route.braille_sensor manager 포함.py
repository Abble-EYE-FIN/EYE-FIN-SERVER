from fastapi import FastAPI, APIRouter, HTTPException, status
from pydantic import BaseModel
from pymongo import MongoClient
import datetime

# Pydantic 모델 정의
class BrailleLang(BaseModel):
    data: str

class FullSensorData(BaseModel):
    # FullSensorData의 실제 필드를 여기에 추가하세요.
    pass

class DBpost(BaseModel):
    id: str
    time: str
    data: str

# MongoDB 설정
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']

# SensorManager 클래스 정의
class SensorManager:
    def interpreteMotion(self, hand: int, data: FullSensorData) -> str:
        # 실제 데이터 해석 로직을 구현합니다.
        return "interpreted_data"

# ESP imu data * (1+1) LR
# MPU imu data on each fingers * (3+3) LR
# ESP shall be reference, calculate relative angle (3mpu 1esp)
# checkout threshold -> binary checkup

# ex) 010 -> a : display in any way --> actuator
# to fast api server, subscribing app
# 'utf-8' string

from utils.imports import *

class SensorManager:
    _flag:str

    def __init__(self) -> None:
        self.ref_msg= [[0]*3]*3
        self.fin_msg= []
        self.ref_msg_http= [[0]*3]*3
        self.fin_msg_http= []
        pass
    
    # message manager for MQTT json format
    def _parse_message(self, message : str):
        self.msg_str = json.load(message)
        # parse all data from json message
        self.ref_msg.clear()
        self._set_reference(self.msg_str["reference"])
        self.fin_msg.clear()
        for i in range(3):
            self._set_fingers(self.msg_str[f"fin{i+1}"])
    
    # message manager for direct http conn
    def _parse_message_http(self, item):
        # parse all data
        self.ref_msg.clear()
        self._set_reference_http(item.reference)
        self.fin_msg.clear()
        self._set_fingers_http(item.finger1)
        self._set_fingers_http(item.finger2)
        self._set_fingers_http(item.finger3)

    def _set_reference(self, message):
        self.ref_msg= [[message["ACC"]["X"],message["ACC"]["Y"],message["ACC"]["Z"]],
                       [message["GYR"]["X"],message["GYR"]["Y"],message["GYR"]["Z"]],
                       [message["MAG"]["X"],message["MAG"]["Y"],message["MAG"]["Z"]]]
    
    def _set_reference_http(self, message: list):
        self.ref_msg = [[message[0],message[1],message[2]],
                        [message[3],message[4],message[5]],
                        [message[6],message[7],message[8]]]
    
    # self.fin_msg[0] : fin1, self.fin_msg[1] : fin2, self.fin_msg[2] : fin3
    def _set_fingers(self, idx, message):
        self.fin_msg.append(
                            [[message["ACC"]["X"],message["ACC"]["Y"],message["ACC"]["Z"]],
                             [message["GYR"]["X"],message["GYR"]["Y"],message["GYR"]["Z"]],
                             [message["MAG"]["X"],message["MAG"]["Y"],message["MAG"]["Z"]]]
                            )
        
    def _set_fingers_http(self, message: list):
        self.fin_msg.append([[message[0], message[1],message[2]],
                             [message[3], message[4],message[5]],
                             [message[6],message[7],message[8]]]
        )

####### common interpreter ########
    def _make_decision(self, idx:int)->int:
        target = self.fin_msg[idx]
        # do calculation with 'self.ref_msg vs target'
        abs_acc_ref = math.sqrt(self.ref_msg[0][0]**2 + self.ref_msg[0][1]**2 + self.ref_msg[0][2]**2)
        abs_acc_fin = math.sqrt(target[0][0]**2 + target[0][1]**2 + target[0][2]**2)
        abs_gyr_ref = math.sqrt(self.ref_msg[1][0]**2 + self.ref_msg[1][1]**2 + self.ref_msg[1][2]**2)
        abs_gyr_fin = math.sqrt(target[1][0]**2 + target[1][1]**2 + target[1][2]**2)

        return 0 #or 1

    def interpreteMotion(self, mode:int, message)->str:
        # all (1+3)*(3,3,3) data set in self variables
        if mode == 0: # MQTT
            self._parse_message(message=message)
        elif mode == 1: # HTTP
            self._parse_message_http(item=message)

        f1 : str = str(self._make_decision(0))
        f2 : str = str(self._make_decision(1))
        f3 : str = str(self._make_decision(2))
        return f1+f2+f3
    

smR = SensorManager()
smL = SensorManager()

# FastAPI 라우터 설정
router = APIRouter()

# POST 엔드포인트 정의
@router.post('/post_right', response_model=DBpost, status_code=status.HTTP_201_CREATED)
def post_right(item: BrailleLang):
    posts = db.posts
    right_post = {
        "id": "bbb",
        "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "data": item.data, 
    }
    post_id = posts.insert_one(right_post)
    return right_post

@router.post('/post_left', response_model=DBpost, status_code=status.HTTP_201_CREATED)
def post_left(item: BrailleLang):
    posts = db.posts
    left_post = {
        "id": "bbb",
        "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "data": item.data, 
    }
    post_id = posts.insert_one(left_post)
    return left_post

@router.post('/post_full_right/', response_model=DBpost, status_code=status.HTTP_200_OK)
def post_full_right(item: FullSensorData):
    data: str = smR.interpreteMotion(1, item)
    posts = db.posts
    right_post = {
        "id": "aaa",
        "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "data": data, 
    }
    post_id = posts.insert_one(right_post)
    return right_post

@router.post('/post_full_left/', response_model=DBpost, status_code=status.HTTP_200_OK)
def post_full_left(item: FullSensorData):
    data: str = smL.interpreteMotion(1, item)
    posts = db.posts
    left_post = {
        "id": "aaa",
        "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "data": data, 
    }
    post_id = posts.insert_one(left_post)
    return left_post

# FastAPI 애플리케이션 설정
app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
