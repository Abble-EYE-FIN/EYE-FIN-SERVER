import uvicorn
import os
from pydantic import BaseModel
from typing import Optional,List
from fastapi.responses import HTMLResponse, FileResponse
from fastapi import FastAPI, status,HTTPException,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles 
from starlette.middleware.cors import CORSMiddleware
from router import route_braille, route_db

app = FastAPI()
app.include_router(route_braille.router)
app.include_router(route_db.router)
app.mount("/static", StaticFiles(directory="static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=["*"]
)

@app.get("/")
def init(request: Request):
    init = "initial page.. wait"
    return init
    # return templates.TemplateResponse("initial.html", {"request": request})

@app.get('/favicon.ico')
async def favicon():
    file_name = "favicon.ico"
    file_path = os.path.join(app.root_path, "static", file_name)
    return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})