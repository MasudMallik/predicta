from jwt import encode,decode,
import datetime
from dotenv import load_dotenv
import os
load_dotenv()


def create_token(data:dict)->str:
    user_data=data.copy()
    user_data["iat"]=datetime.datetime.utcnow()
    user_data["exp"]=datetime.datetime.utcnow()+datetime.timedelta(minutes=30)
    token=encode(user_data,os.getenv("secretkey"),algorithm=os.getenv("algorithm"))
    return token

def decode_token(token:str)->dict:
    try:
        data=decode(token,os.getenv("secretkey"),algorithms=[os.getenv("algorithm")])
    except Exception:
        return {"data":False}
    else:
        return {"data":data}
