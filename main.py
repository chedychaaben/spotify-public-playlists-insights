from getPlaylistDataFromSpotify import getPlaylistDataFromSpotify
from youtubeLinkScrapper import youtubeLinkScrapper
from WebmToMp3 import convert_to_mp3

def main(playlist_id):
    try:
        print("Fetching Spotify playlist data...")
        getPlaylistDataFromSpotify(playlist_id)
        print("Scraping YouTube links and downloading...")
        youtubeLinkScrapper(playlist_id)
        print("Converting files to MP3...")
        convert_to_mp3(f"Playlist_{playlist_id}", f"Playlist_{playlist_id}_MP3")
        print("Process completed successfully!")
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    playlist_id = input("Enter Spotify playlist ID: ")
    main(playlist_id)