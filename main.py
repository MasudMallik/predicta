
from email.message import EmailMessage
import aiosmtplib
import asyncio
import random
async def send_mail():
        r=random.randint(100,200)
        message=EmailMessage()
        message["From"]="predicta.team@gmail.com"
        message["To"]="masudmallik96@gmail.com"
        message["Subject"]="random message"
        message.set_content(f"your otp is {r}")

        await aiosmtplib.send(
            message,
            hostname="smtp.gmail.com",
            port=587,
            start_tls=True,
            username="predicta.team@gmail.com",
            password="hcqxbrwwzmknlehg"
        )


asyncio.run(send_mail())
