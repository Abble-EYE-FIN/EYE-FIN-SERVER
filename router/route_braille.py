from utils.imports import *
from src.SensorManager import SensorManager
from utils.apiutils.models import BrailleLang,DBpost,FullSensorData

# DB client
# This part can be changed into AWS RDB 
client = MongoClient(host='localhost', port=27017)
db = client['brailleDB']

# set this file as router manager
router = APIRouter()

smL = SensorManager()
smR = SensorManager()

# post calculated right hand data [mqtt]
@router.post('/post_right', response_model=DBpost, status_code=status.HTTP_201_CREATED)
def post_right(item : BrailleLang):
    # posts = db.posts
    print(item.data)
    right_post = {
        "id" : "bbb",
        "time" : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "data" : item.data, 
    }
    # post_id = posts.insert_one(right_post)
    return right_post

# post calculated left hand data [mqtt]
@router.post('/post_left', response_model=DBpost, status_code=status.HTTP_201_CREATED)
def post_left(item : BrailleLang):
    # posts = db.posts
    print(item.data)
    left_post = {
        "id" : "bbb",
        "time" : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "data" : item.data, 
    }
    # post_id = posts.insert_one(left_post)
    return left_post

# post right hand data, interpretation takes place here [http]
@router.post('/post_full_right/', response_model=DBpost, status_code=status.HTTP_200_OK)
def post_full_right(item : FullSensorData):
    data: str = smR.interpreteMotion(1,item)
    # posts = db.posts
    right_post = {
        "id" : "aaa",
        "time" : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "data" : data, 
    }
    # post_id = posts.insert_one(right_post)
    return right_post

# post left hand data, interpretation takes place here [http]
@router.post('/post_full_left/', response_model=DBpost, status_code=status.HTTP_200_OK)
def post_full_left(item : FullSensorData):
    data: str = smL.interpreteMotion(1,item)
    # posts = db.posts
    left_post = {
        "id" : "aaa",
        "time" : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "data" : data, 
    }
    # post_id = posts.insert_one(left_post)
    return left_post
