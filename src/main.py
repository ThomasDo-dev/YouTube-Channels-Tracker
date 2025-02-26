import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
CHANNEL_ID = "UC_x5XG1OV2P6uZZ5FSM9Ttw"

url = 'https://www.googleapis.com/youtube/v3/channels'
params = {
    "part": "snippet,statistics",
    "id": CHANNEL_ID,
    "key": API_KEY
}

response = requests.get(url, params=params)
data = response.json()
print(data)
