import requests

class YouTubeAPI:

    def __init__(self):
        self.url = "https://www.googleapis.com/youtube/v3" # YouTube API HTTP endpoint

    def get_channel_subs_and_id(self, channel_handle: str, api_key: str):

        """
        Fetches the subscriber count for a give YouTube channel
        :param channel_handle: The unique identifier of the YouTube channel
        :param api_key: Your YouTube v3 API key
        :return: The subscriber count, the channel id
        """

        # Define the API endpoint for fetching channel data
        url_channel = self.url + "/channels"

        # Set up the parameters for the API request
        params = {
            "part": "statistics, id",
            "forUsername": channel_handle,
            "key": api_key
        }

        # Attempt to make the API call.
        try:
            response = requests.get(url_channel, params=params)
            response.raise_for_status()  # Raises an error for 4xx/5xx status codes
            data = response.json()

            if data.get("items"):
                return data["items"][0]["statistics"]["subscriberCount"], data["items"][0]["id"]
            else:
                print("Error: Empty data")

        except (requests.exceptions.RequestException, ValueError) as e:
            # Handle both HTTP and JSON parsing errors
            print(f"Error: {e}")

        return None


    def get_video_ids_from_channel(self, channel_id: str, api_key: str, rfc3339_time):
        """
        Fetches the videos ids of a channel in the last 6 months excluding shorts
        :param channel_id: The unique identifier of the YouTube channel
        :param api_key: Your YouTube v3 API key
        :param rfc3339_time: Date and time 6 months ago in rfc3339 format
        :return: video ids
        """

        # Define the API endpoint for fetching video data
        url_search = self.url + "/search"

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
            response.raise_for_status()  # Raises an error for 4xx/5xx status codes
            data = response.json()

            if data.get("items"):
                video_ids = [item["id"]["videoId"] for item in data.get("items", [])]
                return video_ids
            else:
                print("Error: Empty data")

        except (requests.exceptions.RequestException, ValueError) as e:
            # Handle both HTTP and JSON parsing errors
            print(f"Error: {e}")

        return None

    def get_video_stats(self, video_id: list, api_key: str):
        """
        Fetches the video content details and stats from a video id list
        :param video_id: The unique identifier of the YouTube video
        :param api_key: Your YouTube v3 API key
        :return: video thumbnail dimension,view counts and comment counts
        """

        # Define the API endpoint for fetching video data
        url_video = self.url + "/videos"

        params = {
            "part": "id, snippet, statistics",
            "id": ",".join(video_id),
            "key": api_key
        }

        try:
            #HTTP request GET
            response = requests.get(url_video, params = params)
            response.raise_for_status()  # Raises an error for 4xx/5xx status codes
            data = response.json()

            if data.get("items"):
                return data.get("items",[])
            else:
                print("Error: Empty data")


        except (requests.exceptions.RequestException, ValueError) as e:
            # Handle both HTTP and JSON parsing errors
            print(f"Error: {e}")