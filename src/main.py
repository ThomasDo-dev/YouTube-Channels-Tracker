import os
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
    videos_wo_shorts = filter_out_shorts(videos_w_stats)
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
    Filter out shorts in the list of videos
    :param video_id: The unique identifier of the YouTube video
    :param api_key: Your YouTube v3 API key
    :return: video thumbnail dimension,view counts and comment counts
    """

    non_shorts = []

    for vid in videos:
        thumbnails = vid.get("snippet", {}).get("thumbnails",{})

        if "default" in thumbnails:
            thumbnail = thumbnails["default"]
            width = thumbnail.get("width", 0)
            height = thumbnail.get("height", 0)

            if width and height and height > width:
                # Video is likely a Short due to vertical aspect ratio
                continue

        non_shorts.append(vid)
        return non_shorts





if __name__ == "__main__":
    main()