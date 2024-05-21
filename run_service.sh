#!/bin/sh

python3 server.py && uvicorn app:app --host 0.0.0.0 --port 8000 --reload