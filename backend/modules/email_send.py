import aiosmtplib
from email.message import EmailMessage
import random
from dotenv import load_dotenv
import os
load_dotenv()

async def send_otp(email:str):
    message=EmailMessage()
    message["From"]=os.getenv("name")
    message["To"]=email
    message["Subject"]="Predicta verification code"
    r=random.randint(100000,999999)
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
        return None
    else:
        return r
