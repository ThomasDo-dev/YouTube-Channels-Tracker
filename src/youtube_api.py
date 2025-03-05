import requests
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta

class YouTubeAPI:

    def __init__(self):
        self.url = 'https://www.googleapis.com/youtube/v3' # YouTube API HTTP endpoint

    def get_subs_and_id(self, channel_handle: str, api_key: str):

        """
        Fetches the subscriber count for a give YouTube channel
        :param channel_handle: The unique identifier of the YouTube channel
        :param api_key: Your YouTube v3 API key
        :return: The subscriber count
        """

        # Define the API endpoint for fetching channel data
        url_channel = self.url + '/channels'

        # Set up the parameters for the API request
        params = {
            "part": "statistics, id",
            "forUsername": channel_handle,
            "key": api_key
        }

        # Attempt to make the API call.
        try:
            response = requests.get(url_channel, params=params)

        except Exception as e:
            print(f"Error:{str(e)}")
            return None

        # Check if the request was successful
        if response.status_code == 200:
            print("HTTP GET Successful")
            try:
                #parse the JSON response
                data = response.json()
                print(data)
            except Exception as e:
                # Handle JSON parsing errors
                print(f"Error parsing JSON: {str(e)}")
                return None

            # Check if 'data' is not empty
            if data:
                return data["items"][0]["statistics"]["subscriberCount"], data["items"][0]["id"]

            else:
                # Print an error if no data is returned
                print("Error: Empty data")
                return None
        else:
            # If the API returns an error status, print out the error details
            print("Error:", response.status_code, response.text)
            return None

    def search_videos_from_channel(self, channel_id: str, api_key: str):

        # Define the API endpoint for fetching video data
        url_search = self.url + '/search'

        # Define the API endpoint for fetching video data
        url_video = self.url + '/video'

        # Get current UTC time
        current_utc_time = datetime.now(timezone.utc)
        # Get time 6 months ago
        time_six_months_ago = current_utc_time - relativedelta(months=6)
        # Convert ro RFC 3339 format
        rfc3339_time = time_six_months_ago.isoformat()

        # Set up the parameters for the API request
        params = {
            "part": "id",
            "channelId": channel_id,
            "type": "video",
            "publishedAfter": rfc3339_time,
            "maxResults": 10,
            "key": api_key
        }

        # Attempt to make the API call.
        try:
            response = requests.get(url_search, params=params)

        except Exception as e:
            print(f"Error:{str(e)}")
            return None

        # Check if the request was successful
        if response.status_code == 200:
            print("HTTP GET Successful")
            try:
                # parse the JSON response
                data = response.json()
                print(data)
            except Exception as e:
                # Handle JSON parsing errors
                print(f"Error parsing JSON: {str(e)}")
                return None
        else:
            # If the API returns an error status, print out the error details
            print("Error:", response.status_code, response.text)
            return None

