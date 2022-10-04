import json
from fastapi import APIRouter,Request,Response
from env import env

router = APIRouter()



@router.post('/webhook')
async def recive_webhook(request: Request):
    return Response(status_code=200)

@router.get('/webhook')
async def get_webhook(request: Request):
    verify_token = env.VERIFY_TOKEN
    # fb_token = request.query_params.get("hub.verify_token") 