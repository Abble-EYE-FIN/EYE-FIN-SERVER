from utils.imports import *
from utils.apiutils.models import BrailleLang,DBpost

client = MongoClient(host='localhost', port=27017)
router = APIRouter()
db = client['brailleDB']

@router.post('/post_left/', response_model=DBpost, status_code=status.HTTP_200_OK) # response_model=OpenCafe
def post_left(item : BrailleLang):
    # posts = db.posts
    # left_post = {
    #     "time" : datetime.datetime.now(),
    #     "data" : data, 
    # }
    # post_id = posts.insert_one(left_post)
    return True

@router.post('/post_right/', response_model=DBpost, status_code=status.HTTP_200_OK) # response_model=OpenCafe
def post_right(item : BrailleLang):
    # posts = db.posts
    # right_post = {
    #     "time" : datetime.datetime.now(),
    #     "data" : data, 
    # }
    # post_id = posts.insert_one(right_post)
    return True