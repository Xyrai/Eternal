import os

from dotenv import load_dotenv, find_dotenv
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse

from lib.erbs_api import ERBSApi

load_dotenv(find_dotenv())

api_key = os.environ['ERBSKey']
router = APIRouter()
ERBS_api = ERBSApi(api_key)


@router.get("/", response_class=HTMLResponse)
def home():
    return f"<body><h1>Eternal API made by Kinesey</h1></body>"


@router.get("/user/nickname")
def get_user_number(nickname: str):
    try:
        user_num = ERBS_api.get_user_num_by_nickname(nickname)
        return user_num
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
