import time, json
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.by import By
from youtubeDownloadModule import download_vid_with_pytube

#Chrome Driver loading ...
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(executable_path=f'chromedriver.exe' ,chrome_options=chrome_options)
browser.maximize_window()

def scrape_song(songObject):
    # Example of entered songObject = {'id': songId,'title' : songTitle, 'artist': songArtist}
    song_name = songObject['title'] + " " + songObject['artist']
    song_search_url = f'https://www.youtube.com/results?search_query={song_name}'
    browser.get(song_search_url)
    time.sleep(5)
    first_vid_box = browser.find_elements(By.TAG_NAME, "ytd-video-renderer")[0] # Get the first video section
    first_vid_box_link = first_vid_box.find_elements(By.TAG_NAME, "a")[0].get_attribute('href') #Get_first_Inker_Tag_href_value
    print(colored(first_vid_box_link, 'red'))
    # Download Now
    download_vid_with_pytube(first_vid_box_link)

data = []
# Output to excel
def load_json_data(file_name):
    global data
    with open(file_name, 'r', encoding='UTF8') as f:
        data = json.load(f)
    print(colored("JSON Data Loaded Successfully","red"))


def youtubeLinkScrapper(playlist_id : str):
    load_json_data(f'playlist-{playlist_id}.json')
    for songObject in data:
        scrape_song(songObject)


