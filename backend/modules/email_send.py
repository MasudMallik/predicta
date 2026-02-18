import asyncio
import random
import aiosmtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
load_dotenv()
async def send_message(email:str):
    code=random.randint(100000,999999)
    message=EmailMessage()
    message["From"]=os.getenv("name")
    message["To"]=email
    message["Subject"]="Predicta Verification Code"
    message.set_content(f"Welcome to Predicta,Your one-time verification code is: {code}This code expires after 5 minutes.Do not share this otp with any one.")
    await aiosmtplib.send(
        message,
        hostname=os.getenv("hostname"),
        port=587,
        start_tls=True,
        username=os.getenv("name"),
        password=os.getenv("password")
    )
    return code
    

def send_otp(email:str):
    try:
        code=asyncio.run(send_message(email))
    except Exception:
        print("message not sent")
    else:
        print("message succesfully send: ",code)
