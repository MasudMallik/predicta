from fastapi import FastAPI, Form, BackgroundTasks
from modules.email_send import send_otp
from upstash_redis import Redis
from dotenv import load_dotenv
import os
import aiosmtplib
from email.message import EmailMessage
import random


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
async def get_user( email: str = Form(...)):
    message=EmailMessage()
    message["From"]=os.getenv("name")
    message["To"]=email
    message["Subject"]="Predicta verification code"
    r=random.randint(000000,999999)
    try:
        message.set_content(f"""Hello,

            Welcome to Predicta! To complete your verification, please use the following one-time password (OTP):

            🔑 Your OTP: {r}

            This code will expire in 5 minutes. For your security, do not share this code with anyone.

            If you did not request this verification, please ignore this message.

            Thank you,
            The Predicta Team
            """)
        await aiosmtplib.send(
            message,
            hostname=os.getenv("hostname"),
            username=os.getenv("name"),
            use_tls=True,
            password=os.getenv("password")
        )
    except Exception:
        return {"otp":"not send"}
    else:
        redis_.setex(f"otp:{email}",180,r)
        return {"otp":r}


@app.post("/reg")
async def register(email: str = Form(...), otp: str = Form(...)):
    prev_otp = redis_.get(f"otp:{email}")
    print(prev_otp)
    if prev_otp == otp:
        return {"status": "login"}
    else:
        return {"status": "otp mismatch"}
