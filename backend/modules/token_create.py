from jwt import encode,decode
from dotenv import load_dotenv
import os
import datetime
load_dotenv()

def create_token(data:dict)->bytes:
    user_det=data.copy()
    user_det["iat"]=datetime.datetime.utcnow()
    user_det["exp"]=datetime.datetime.utcnow()+datetime.timedelta(minutes=30)
    token=encode(user_det,os.getenv("secretkey"),algorithm=os.getenv("algorithm"))
    return token

def decode_token(token:bytes)->dict:
    try:
        data=decode(token,os.getenv("secretkey"),algorithms=[os.getenv("algorithm")])
    except Exception:
        return None
    else:
        return data