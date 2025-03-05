import os
from dotenv import load_dotenv
from youtube_api import YouTubeAPI

def main():
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    CHANNEL_HANDLE = "GoogleDevelopers"

    a = YouTubeAPI()
    subscriber_count, channel_id = a.get_subs_and_id(CHANNEL_HANDLE, API_KEY)
    print(f'Subscriber Count: {subscriber_count}')
    print(f'Channel ID: {channel_id}\n')
    channel_videos_data = a.search_videos_from_channel(channel_id, API_KEY)
    if channel_videos_data:
        print(channel_videos_data)

if __name__ == "__main__":
    main()