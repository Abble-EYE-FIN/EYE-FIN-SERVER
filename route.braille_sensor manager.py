from fastapi import APIRouter, status
from pymongo import MongoClient
import datetime
from pydantic import BaseModel

# SensorManager 클래스 정의
class SensorManager:
    def __init__(self, thresholds=None):
        # 기본 임계값 설정 (필요에 따라 조정 가능)
        if thresholds is None:
            thresholds = {
                'index': 8.0,
                'middle': 8.0,
                'ring': 7.0,
                'pinky': 6.0
            }
        self.thresholds = thresholds

    def interpreteMotion(self, hand_id, sensor_data):
        """
        손의 움직임을 해석하고 특정 동작을 반환하는 함수
        :param hand_id: 손 ID (1=오른손, 2=왼손)
        :param sensor_data: 센서 데이터
        :return: 해석된 동작 (문자열)
        """
        acc_X = sensor_data.acc_X
        acc_Y = sensor_data.acc_Y
        acc_Z = sensor_data.acc_Z
        
        # 동작 해석 로직
        if acc_X > self.thresholds['index']:
            return "Index Finger Action"
        elif acc_Y > self.thresholds['middle']:
            return "Middle Finger Action"
        elif acc_Z > self.thresholds['ring']:
            return "Ring Finger Action"
        # 필요에 따라 더 많은 조건 추가 가능
        else:
            return "No significant action detected"

# Pydantic 모델 정의 (데이터 구조)
class BrailleLang(BaseModel):
    data: str

class FullSensorData(BaseModel):
    acc_X: float
    acc_Y: float
    acc_Z: float

class DBpost(BaseModel):
    id: str
    time: str
    data: str

# MongoDB 클라이언트 설정
client = MongoClient(host='localhost', port=27017)
db = client['brailleDB']

# APIRouter 설정
router = APIRouter()

# SensorManager 인스턴스 생성 (임계값을 지정할 수 있습니다.)
smL = SensorManager()  # 왼손 센서 매니저
smR = SensorManager()  # 오른손 센서 매니저

# 오른손 데이터를 처리하여 해석된 결과를 반환 [MQTT]
@router.post('/post_right', response_model=DBpost, status_code=status.HTTP_201_CREATED)
def post_right(item: BrailleLang):
    print(item.data)
    right_post = {
        "id": "bbb",
        "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "data": item.data,
    }
    return right_post

# 왼손 데이터를 처리하여 해석된 결과를 반환 [MQTT]
@router.post('/post_left', response_model=DBpost, status_code=status.HTTP_201_CREATED)
def post_left(item: BrailleLang):
    print(item.data)
    left_post = {
        "id": "bbb",
        "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%:M:%S'),
        "data": item.data,
    }
    return left_post

# 오른손의 전체 센서 데이터를 받아 해석 후 반환 [HTTP]
@router.post('/post_full_right/', response_model=DBpost, status_code=status.HTTP_200_OK)
def post_full_right(item: FullSensorData):
    data: str = smR.interpreteMotion(1, item)
    right_post = {
        "id": "aaa",
        "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "data": data,
    }
    return right_post

# 왼손의 전체 센서 데이터를 받아 해석 후 반환 [HTTP]
@router.post('/post_full_left/', response_model=DBpost, status_code=status.HTTP_200_OK)
def post_full_left(item: FullSensorData):
    data: str = smL.interpreteMotion(1, item)
    left_post = {
        "id": "aaa",
        "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "data": data,
    }
    return left_post
