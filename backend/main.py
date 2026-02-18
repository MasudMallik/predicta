from fastapi import FastAPI,Request,HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer
from modules.email_send import send_otp
from modules.hashed_password import hash_pw,check_password
from modules.token_create import create_token,decode_token

app=FastAPI(title="Predicta",
            description="this is a combination of multiple ml models..",
            version="0.0.0.1")
outh2=OAuth2PasswordBearer(tokenUrl="token")