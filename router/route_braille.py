from utils.imports import *

client = MongoClient(host='localhost', port=27017)
router = APIRouter()
db = client['brailleDB']

@router.post('/post_left/', status_code=status.HTTP_200_OK) # response_model=OpenCafe
def post_left(data : str):
    posts = db.posts
    left_post = {
        "time" : datetime.datetime.now(),
        "data" : data, 
    }
    post_id = posts.insert_one(left_post)
    return

@router.post('/post_right/', status_code=status.HTTP_200_OK) # response_model=OpenCafe
def post_right(data : str):
    posts = db.posts
    right_post = {
        "time" : datetime.datetime.now(),
        "data" : data, 
    }
    post_id = posts.insert_one(right_post)
    return