import time, json
from termcolor import colored
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def scrape_song(song, data):
    second_comuln = song.find_element(By.CLASS_NAME, 'iCQtmPqY0QvkumAOuCjr')
    songId      = song.find_element(By.CLASS_NAME, 'VpYFchIiPg3tPhBGyynT').get_attribute('innerText')
    songTitle   = second_comuln.find_element(By.TAG_NAME, 'a').get_attribute('innerText')
    songArtist  = second_comuln.find_elements(By.TAG_NAME, 'span')[len(second_comuln.find_elements(By.TAG_NAME, 'span'))-1].get_attribute('innerText')
    
    songDict = {
                'id': songId,
                'title' : songTitle, 
                'artist': songArtist
            }
    if songDict not in data:
        data.append(songDict)
        print(colored(f'Scraped Song: -{songId}- {songTitle} - {songArtist}', 'yellow'))

def scroll_to_element(songsWebElement, element_id,browser):
    print(colored( f'Scrolling To Index of Last Loaded song : {element_id}', 'green'))
    ActionChains(browser)\
        .scroll_to_element(songsWebElement[element_id-1])\
        .perform()
    #It returns the id of the last availble song
    lastLoadedSongId      = songsWebElement[element_id-1].find_element(By.CLASS_NAME, 'VpYFchIiPg3tPhBGyynT').get_attribute('innerText')
    lastLoadedSongTitle   = songsWebElement[element_id-1].find_element(By.CLASS_NAME, 'iCQtmPqY0QvkumAOuCjr').find_element(By.TAG_NAME, 'a').get_attribute('innerText')
    lastLoadedSongArtist  = songsWebElement[element_id-1].find_element(By.CLASS_NAME, 'iCQtmPqY0QvkumAOuCjr').find_element(By.TAG_NAME, 'span').get_attribute('innerText')
    print(colored( 'Scrolled To : ', 'green'), colored(f'Scraped Song: -{lastLoadedSongId}- {lastLoadedSongTitle} - {lastLoadedSongArtist}', 'yellow'))
    return lastLoadedSongId

last_time_index = 0

# Output to excel
def output_to_json(data, playlist_id):
    with open(f'playlist-{playlist_id}.json', 'w', encoding='UTF8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(colored("Outputted to JSON file Successfully","red"))


def getPlaylistDataFromSpotify(playlist_id : str):
    playlist_url = f'https://open.spotify.com/playlist/{playlist_id}'
    #Chrome Driver loading ...
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(executable_path=f'chromedriver.exe' ,chrome_options=chrome_options)
    browser.maximize_window()

    browser.get(playlist_url)
    data = []


    print('Waiting for contentSpacing div that contains the songs to load ')
    time.sleep(10)
    print('10 seconds passed, Lets risk that its okay and loaded')

    Ks = browser.find_elements(By.CLASS_NAME, "JUa6JJNj7R_Y3i4P8YUX")[0] #browser.find_elements(By.CLASS_NAME, "contentSpacing")
    last_song_name = ""
    while True:
        #get_availble_songs on the first check
        songsContainer = Ks.find_elements(By.CLASS_NAME, 'h4HgbO_Uu1JYg5UGANeQ')
        # Scrape from 0 to len(songs)
        for songRow in songsContainer:
            scrape_song(songRow,data)
        
        global last_time_index

        this_lastLoadedSongId = scroll_to_element(songsContainer, len(songsContainer), browser)
        if last_time_index == this_lastLoadedSongId:
            break
        last_time_index = this_lastLoadedSongId

        time.sleep(5)
    output_to_json(data, playlist_id)