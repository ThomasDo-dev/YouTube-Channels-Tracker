import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
from youtube_api import YouTubeAPI




def main():
    load_dotenv()

    API_KEY = os.getenv("API_KEY")
    CHANNEL_HANDLE = "GoogleDevelopers"
    time_six_months_ago = date_x_months_ago(6)
    a = YouTubeAPI()

    subscriber_count, channel_id = a.get_channel_subs_and_id(CHANNEL_HANDLE, API_KEY)
    print(f'Subscriber Count: {subscriber_count}')
    print(f'Channel ID: {channel_id}\n')

    channel_videos_ids = a.get_video_ids_from_channel(channel_id, API_KEY, time_six_months_ago)
    print(channel_videos_ids)

    videos_w_stats = a.get_video_stats(channel_videos_ids,API_KEY)
    print(videos_w_stats)
    videos_wo_shorts = filter_out_shorts(channel_videos_ids)
    print(videos_wo_shorts)






def date_x_months_ago(months: int):
    """
    Get date and time of x months in rfc3339 format
    :param months: An integer value of how many months back the user want to look back at
    :return: rfc3339_time of x months ago
    """
    # Get current UTC time
    current_utc_time = datetime.now(timezone.utc)
    # Get time x months ago
    time_six_months_ago = current_utc_time - relativedelta(months=months)
    # Convert to RFC 3339 format
    rfc3339_time = time_six_months_ago.isoformat()
    return rfc3339_time

def filter_out_shorts(videos):
    """
    Filters out Shorts from a list of video IDs.
    :param videos: List of video IDs as strings.
    :return: List of video IDs that are not identified as Shorts.
    """
    non_shorts = []
    for vid in videos:
        url = "https://www.youtube.com/shorts/" + vid
        try:
            response = requests.head(url, timeout=5)
        except Exception as e:
            print(f"Error for video {vid}: {e}")
            # Append either way so don't mistakenly filter out video due to bad network
            non_shorts.append(vid)
            continue
        # If the status code is 200, assume it's a Short and skip it.
        if response.status_code == 200:
            continue
        non_shorts.append(vid)
    return non_shorts





if __name__ == "__main__":
    main()