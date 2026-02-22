from fastapi import FastAPI, Form, BackgroundTasks
from modules.email_send import send_otp
from upstash_redis import Redis
from dotenv import load_dotenv
import os
load_dotenv()


app = FastAPI()
redis_ = Redis(url=os.getenv("redis_url"),token=os.getenv("redis_token"))

async def otp_gen(email: str):
    otp = await send_otp(email)
    if otp:
        redis_.setex(f"otp:{email}", 300, str(otp))
    else:
        redis_.setex(f"otp:{email}", 300, None)

@app.post("/")
async def get_user(background_tasks: BackgroundTasks, email: str = Form(...)):
    background_tasks.add_task(otp_gen,email)
    return {"status": "OTP task scheduled"}

@app.post("/reg")
async def register(email: str = Form(...), otp: str = Form(...)):
    prev_otp = redis_.get(f"otp:{email}")
    print(prev_otp)
    if prev_otp == otp:
        return {"status": "login"}
    else:
        return {"status": "otp mismatch"}
