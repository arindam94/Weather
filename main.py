import requests
from twilio.rest import Client
import os

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
openweather_api_key = os.environ.get("OPENWEATHER_API_KEY")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
print("SID:", account_sid)
print("Token exists:", auth_token is not None)
print("Token length:", len(auth_token) if auth_token else 0)
prameter = {
    "lat": "22.5726",
    "lon": "88.3639",
    "appid": openweather_api_key,
    "cnt": 4
}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast',prameter)
response.raise_for_status()
print(response.json())
json_data = response.json()
for item in json_data['list']:
    if item['weather'][0]["id"] < 700:
        print("Its rainign please bring umbrella")
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body= "sms_event_notifications",
            from_="+17372508034",
            to="+918145981844"
        )
        print(message.status)
    else:
        print("Its sunny weather")

