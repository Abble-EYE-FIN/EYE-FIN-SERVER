import os
from fastapi import APIRouter, Request, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Optional, List
import json

router = APIRouter()

@router.post('/post_left/', status_code=status.HTTP_200_OK) # response_model=OpenCafe
def post_left():
    return

@router.post('/post_right/', status_code=status.HTTP_200_OK) # response_model=OpenCafe
def post_right():
    return