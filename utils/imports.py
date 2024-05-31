import paho.mqtt.client as mqtt
from datetime import datetime
from dataclasses import dataclass
from typing import SupportsFloat
import time
import math
import socket
import json
import requests
import os
import datetime
from fastapi import APIRouter, Request, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Optional, List
import json
from pymongo import MongoClient