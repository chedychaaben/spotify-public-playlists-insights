import time
import json
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

def scrape_song(song, data):
    try:
        song_id = song.find_element(By.CSS_SELECTOR, "div[data-testid='track-row'] div[data-testid='tracklist-row__track-id']").text
        title_elem = song.find_element(By.CSS_SELECTOR, "div[data-testid='tracklist-row__track-info'] a")
        song_title = title_elem.text
        artist_elem = song.find_element(By.CSS_SELECTOR, "div[data-testid='tracklist-row__track-info'] span:last-child")
        song_artist = artist_elem.text
        song_dict = {'id': song_id, 'title': song_title, 'artist': song_artist}
        if song_dict not in data:
            data.append(song_dict)
            print(colored(f"Scraped Song: -{song_id}- {song_title} - {song_artist}", 'yellow'))
    except Exception as e:
        print(colored(f"Error scraping song: {e}", "red"))

def scroll_to_element(songs, element_id, browser):
    try:
        print(colored(f"Scrolling to index: {element_id}", 'green'))
        ActionChains(browser).scroll_to_element(songs[element_id-1]).perform()
        last_song = songs[element_id-1]
        last_id = last_song.find_element(By.CSS_SELECTOR, "div[data-testid='track-row'] div[data-testid='tracklist-row__track-id']").text
        last_title = last_song.find_element(By.CSS_SELECTOR, "div[data-testid='tracklist-row__track-info'] a").text
        last_artist = last_song.find_element(By.CSS_SELECTOR, "div[data-testid='tracklist-row__track-info'] span:last-child").text
        print(colored(f"Scrolled to: -{last_id}- {last_title} - {last_artist}", 'yellow'))
        return last_id
    except Exception as e:
        print(colored(f"Error scrolling: {e}", "red"))
        return None

def output_to_json(data, playlist_id):
    try:
        with open(f'playlist-{playlist_id}.json', 'w', encoding='UTF8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(colored("Outputted to JSON file Successfully", "red"))
    except Exception as e:
        print(colored(f"Error saving JSON: {e}", "red"))

def getPlaylistDataFromSpotify(playlist_id: str):
    playlist_url = f'https://open.spotify.com/playlist/{playlist_id}'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.maximize_window()

    try:
        browser.get(playlist_url)
        print("Waiting for playlist to load...")
        WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='tracklist-row']"))
        )
        data = []
        last_time_index = None
        while True:
            songs = browser.find_elements(By.CSS_SELECTOR, "div[data-testid='tracklist-row']")
            for song in songs:
                scrape_song(song, data)
            if not songs:
                print(colored("No songs found.", "red"))
                break
            new_last_id = scroll_to_element(songs, len(songs), browser)
            if new_last_id == last_time_index:
                break
            last_time_index = new_last_id
            time.sleep(1)  # Brief pause to allow new content to load
        output_to_json(data, playlist_id)
    except Exception as e:
        print(colored(f"Error in scraping playlist: {e}", "red"))
    finally:
        browser.quit()

if __name__ == "__main__":
    playlist_id = input("Enter Spotify playlist ID: ")
    getPlaylistDataFromSpotify(playlist_id)