import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    CHANNEL_HANDLE = "GoogleDevelopers"


if __name__ == "main":
    main()