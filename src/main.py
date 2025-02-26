import os
from dotenv import load_dotenv
from youtube_api import YouTubeAPI

def main():
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    CHANNEL_HANDLE = "GoogleDevelopers"

    a = YouTubeAPI()
    subscriber_count = a.get_statistics(CHANNEL_HANDLE, API_KEY)
    print("Subscriber Count:", subscriber_count)


if __name__ == "__main__":
    main()