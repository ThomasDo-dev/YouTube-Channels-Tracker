import os
from dotenv import load_dotenv
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
from youtube_api import YouTubeAPI

def main():
    load_dotenv()

    API_KEY = os.getenv("API_KEY")
    CHANNEL_HANDLE = "GoogleDevelopers"
    time_six_months_ago = six_months_ago()
    a = YouTubeAPI()

    subscriber_count, channel_id = a.get_subs_and_id(CHANNEL_HANDLE, API_KEY)

    print(f'Subscriber Count: {subscriber_count}')
    print(f'Channel ID: {channel_id}\n')

    channel_videos_data = a.search_videos_from_channel(channel_id, API_KEY, time_six_months_ago)

    if channel_videos_data:
        print(channel_videos_data)

def six_months_ago():
    # Get current UTC time
    current_utc_time = datetime.now(timezone.utc)
    # Get time 6 months ago
    time_six_months_ago = current_utc_time - relativedelta(months=6)
    # Convert ro RFC 3339 format
    rfc3339_time = time_six_months_ago.isoformat()
    return rfc3339_time

if __name__ == "__main__":
    main()