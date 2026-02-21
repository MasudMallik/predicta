from fastapi import FastAPI, Form, BackgroundTasks
from modules.email_send import send_otp
from redis import Redis

app = FastAPI()
redis_ = Redis(host="localhost", port=6379, decode_responses=True)

def otp_gen(email: str):
    otp = send_otp(email)
    if otp:
        redis_.setex(f"otp:{email}", 300, str(otp))

@app.post("/")
async def get_user(background_tasks: BackgroundTasks, email: str = Form(...)):
    background_tasks.add_task(otp_gen, email)
    return {"status": "OTP task scheduled"}

@app.post("/reg")
async def register(email: str = Form(...), otp: str = Form(...)):
    prev_otp = redis_.get(f"otp:{email}")
    if prev_otp == otp:
        return {"status": "login"}
    else:
        return {"status": "otp mismatch"}
