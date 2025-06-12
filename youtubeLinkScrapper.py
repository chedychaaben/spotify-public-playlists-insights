import time
import json
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from youtubeDownloadModule import download_vid_with_pytube

def init_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.maximize_window()
    return browser

def scrape_song(song_object, folder_name, browser):
    try:
        song_name = f"{song_object['title']} {song_object['artist']}"
        song_search_url = f'https://www.youtube.com/results?search_query={song_name}'
        browser.get(song_search_url)
        time.sleep(3)
        videos = browser.find_elements(By.TAG_NAME, "ytd-video-renderer")
        if not videos:
            print(colored(f"No videos found for {song_name}", "red"))
            return
        first_vid_link = videos[0].find_elements(By.TAG_NAME, "a")[0].get_attribute('href')
        print(colored(first_vid_link, 'yellow'))
        download_vid_with_pytube(first_vid_link, folder_name)
        print(colored(f"{song_name} OK", 'green'))
    except Exception as e:
        print(colored(f"Error scraping {song_name}: {e}", "red"))

def load_json_data(file_name):
    try:
        with open(file_name, 'r', encoding='UTF8') as f:
            return json.load(f)
    except Exception as e:
        print(colored(f"Error loading JSON: {e}", "red"))
        raise

def youtubeLinkScrapper(playlist_id: str):
    data = load_json_data(f'playlist-{playlist_id}.json')
    folder_name = f"Playlist_{playlist_id}"
    browser = init_browser()
    try:
        for song_object in data:
            scrape_song(song_object, folder_name, browser)
    finally:
        browser.quit()
    print(colored("Scraping and downloading completed", "green"))