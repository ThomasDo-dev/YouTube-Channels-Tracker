import requests

class YouTubeAPI:

    def __init__(self):
        pass

    def get_statistics(self, channel_handle: str, api_key: str):

        """
        Fetches the subscriber count for a give YouTube channel
        :param channel_handle: The unique identifier of the YouTube channel
        :param api_key: Your YouTube v3 API key
        :return: The subscriber count
        """

        # Define the API endpoint for fetching channel data
        url = 'https://www.googleapis.com/youtube/v3/channels'

        # Set up the parameters for the API request
        params = {
            "part": "statistics",
            "forUsername": channel_handle,
            "key": api_key
        }

        # Attempt to make the API call.
        try:
            response = requests.get(url, params=params)

        except Exception as e:
            print(f"Error:{str(e)}")
            return None

        # Check if the request was successful
        if response.status_code == 200:
            print("HTTP Request Successful")
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
                return data["items"][0]["statistics"]["subscriberCount"]
            else:
                # Print an error if no data is returned
                print("Error: Empty data")
                return None
        else:
            # If the API returns an error status, print out the error detials
            print("Error:", response.status_code, response.text)
            return None
