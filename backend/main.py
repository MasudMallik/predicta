from fastapi import FastAPI,Request,Form,Depends,BackgroundTasks
from modules.email_send import send_otp
from fastapi.security import OAuth2PasswordBearer
from redis import Redis
redis_=Redis(host="localhost",port=6379,decode_responses=True)

app=FastAPI()

async def otp_gen(email):
    otp=await send_otp(email)
    redis_.setex("otp",60,str(otp))

@app.post("/")
async def get_user(background  :BackgroundTasks,email:str=Form(...)):
    background.add_task(otp_gen,email)
    return {"otp":redis_.get("otp")}

@app.post("/reg")
async def register(otp:str):
    prev_otp=redis_.get("otp")
    print(prev_otp)
    if prev_otp==otp:
        print("login")
    else:
        print("otp missmatch")