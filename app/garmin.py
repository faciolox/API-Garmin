import os
import requests,json
from datetime import date
from dateutil.relativedelta import relativedelta
API_KEY = os.getenv("GARMIN_API_KEY")# meglio non scriverla nel codice

BASE = "https://personal.connectapi.garmin.com"


def get_token():
    url = "https://personal.connectapi.garmin.com/personalapitoken-service/personal-api/personal-api-key/token"
    headers = {"Authorization": f"ApiKey {API_KEY}"}

    resp = requests.post(url, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.text


def get_summary():
    yesterday = date.today() - relativedelta(days=1)
    out = requests.get(
    f"{BASE}/usersummary-service/usersummary/daily",
    headers={"Authorization": f"Bearer {get_token()}",
             "Accept": "application/json"},
    params={"calendarDate": yesterday.isoformat()},  # formato AAAA-MM-GG
    timeout=30,
    )
    out = out.text
    out = json.loads(out)
    return out

"""def get_summary(date:date):
    
    out = requests.get(
    f"{BASE}/usersummary-service/usersummary/daily",
    headers={"Authorization": f"Bearer {get_token()}",
             "Accept": "application/json"},
    params={"calendarDate": date.isoformat()},  # formato AAAA-MM-GG
    timeout=30,
    )
    out = out.text
    out = json.loads(out)
    return out"""
# o resp.text se la risposta non è JSON