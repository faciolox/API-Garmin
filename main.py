import app.garmin as garmin
import os,json
import smtplib
from email.message import EmailMessage

msg= EmailMessage()
msg["From"] = os.getenv("MAIL")
msg["To"] = os.getenv("MAIL")
msg["Subject"] = "[Garmin] Riepilogo di ieri"
riepilogo = garmin.get_summary()
msg.set_content(json.dumps(riepilogo,indent=4,ensure_ascii=False))
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.set_debuglevel(1)
    server.login(os.getenv("MAIL"), os.getenv("GMAIL_PSW"))
    server.send_message(msg)