import os

from dotenv import load_dotenv, find_dotenv
from fastapi import APIRouter, HTTPException

from lib.erbs_api import ERBSApi

load_dotenv(find_dotenv())

api_key = os.environ['ERBSKey']
ERBS_api = ERBSApi(api_key)

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/nickname")
def get_user_number(nickname: str):
    try:
        user_num = ERBS_api.get_user_num_by_nickname(nickname)
        return user_num
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
