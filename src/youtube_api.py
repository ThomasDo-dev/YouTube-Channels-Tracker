import requests

class YouTubeAPI:

    def __init__(self):
        pass

    def get_statistics(self, channel_handle: str, api_key: str):

        url = 'https://www.googleapis.com/youtube/v3/channels'

        params = {
            "part": "statistics",
            "id": channel_handle,
            "key": api_key
        }

        try:
            response = requests.get(url, params=params)

        except Exception as e:
            print(f"Error:{str(e)}")
            return None

        # Check if the request was successful
        if response.status_code == 200:
            try:
                data = response.json()

            except Exception as e:
                print(f"Error:{str(e)}")
                return None
            if data:
                return data["items"][0]["statistics"]["subscriberCount"]
            else:
                print("Error: Empty data")
        else:
            print("Error:", response.status_code, response.text)
