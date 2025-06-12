# 🎵 Spotify Playlist Downloader 🎧

Welcome to the **Spotify Playlist Downloader**! 🚀 This Python tool scrapes song details (title, artist) from a Spotify playlist 🌐, searches for matching videos on YouTube 🎥, downloads their audio 🎶, and converts them to MP3 format 🎵. It uses Selenium for web scraping, `pytube` and `yt-dlp` for downloading, and `ffmpeg` for audio conversion. Let's get your favorite playlists saved as MP3s! 😎

## ✨ Features
- Scrapes song titles and artists from Spotify playlists using Selenium 🕵️‍♂️
- Searches YouTube for each song and downloads the audio of the first result 📥
- Converts downloaded audio files (`.webm` or `.mp4`) to MP3 format 🔄
- Saves song metadata to a JSON file for easy reference 📝
- Cross-platform compatible with robust error handling 🛠️

## 🛠️ Prerequisites
- **Python 3.8+** 🐍
- **ffmpeg**: Must be installed and added to your system PATH 📦
  - Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html) or run `choco install ffmpeg`
  - Linux: `sudo apt-get install ffmpeg`
  - macOS: `brew install ffmpeg`
- A web browser (Chrome recommended) for Selenium 🌐

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Verify `ffmpeg` is installed:
   ```bash
   ffmpeg -version
   ```

## 📋 Dependencies
Listed in `requirements.txt`:
```
yt-dlp
pytube
selenium
termcolor
webdriver-manager
```

## 🗂️ Project Structure
- `main.py`: Orchestrates the entire workflow (scrape, download, convert) 🎮
- `getPlaylistDataFromSpotify.py`: Scrapes song details from Spotify 📋
- `youtubeLinkScrapper.py`: Finds YouTube videos and downloads audio 🎥
- `youtubeDownloadModule.py`: Handles audio downloads with `pytube` and `yt-dlp` 📥
- `WebmToMp3.py`: Converts audio files to MP3 using `ffmpeg` 🔄
- `requirements.txt`: Lists required Python packages 📦

## 🚀 Usage
1. Run the main script:
   ```bash
   python main.py
   ```
2. Enter a Spotify playlist ID (e.g., `37i9dQZF1DXcBWIGoYBM5M` from `https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M`) when prompted 🎯
3. The script will:
   - Scrape song details and save to `playlist-<id>.json` 📝
   - Download audio files to `Playlist_<id>` folder 📥
   - Convert files to MP3 and save in `Playlist_<id>_MP3` folder 🎵

## 🎉 Example
```bash
$ python main.py
Enter Spotify playlist ID: 37i9dQZF1DXcBWIGoYBM5M
Fetching Spotify playlist data... 🌐
Scraped Song: -12345- Song Title - Artist Name 🎶
...
Outputted to JSON file Successfully 📝
Scraping YouTube links and downloading... 🎥
https://www.youtube.com/watch?v=abc123
Download complete: Song Title.mp3 📥
Converting files to MP3... 🔄
Converted Song Title.webm to MP3 🎵
Process completed successfully! 🎉
```

## 🛠️ Improvements Made
The original code had some hiccups, but we've polished it up! 💪 Here's what we did:
- **Selenium Reliability**: Swapped fragile class selectors for stable `data-testid` attributes and added `WebDriverWait` for dynamic loading ⏳
- **Library Updates**: Replaced `youtube_dl` with `yt-dlp` (more reliable) and fixed `pytube` stream filtering for consistent downloads 🔗
- **Cross-Platform Paths**: Used `os.path.join` for file paths to work on Windows, Linux, and macOS 🌍
- **Error Handling**: Added try-except blocks for network issues, missing elements, and file operations 🛡️
- **Browser Efficiency**: Reused a single Selenium browser instance for YouTube scraping to save resources ⚡
- **File Conversion**: Updated `WebmToMp3.py` to handle `.webm` and `.mp4` extensions and removed `shell=True` for security 🔒
- **Workflow Integration**: Automated MP3 conversion in `main.py` for a seamless experience 🤖
- **No API Dependency**: Stuck with web scraping for Spotify data, as requested 🚫

## 🐛 Troubleshooting
- **Selenium Errors**: If Spotify’s layout changes, inspect the playlist page (F12 in browser) to update `data-testid` selectors in `getPlaylistDataFromSpotify.py` 🔍
- **Download Failures**: If `pytube` fails, try switching to `yt-dlp` in `youtubeLinkScrapper.py` by calling `download_vid_with_yt_dlp` 🔄
- **ffmpeg Errors**: Ensure `ffmpeg` is in PATH (`ffmpeg -version`). Install if missing 📦
- **Slow Scraping**: Adjust `time.sleep` in `youtubeLinkScrapper.py` or add `WebDriverWait` for network delays ⏲️
- **Large Playlists**: Test with a small playlist (5-10 songs) first to confirm everything works smoothly ✅

## ⚠️ Notes
- **Legal Notice**: Downloading audio from YouTube may violate their terms of service unless you have permission. Use responsibly! ⚖️
- **Spotify DOM Changes**: Spotify’s web interface may update, breaking selectors. Check `data-testid` attributes periodically 🔧
- **Performance**: Web scraping is slower than an API. Large playlists may take time due to scrolling and page loads 🐢

## 🤝 Contributing
We’d love your help to make this tool even better! 🌟 Submit issues or pull requests for:
- Support for additional audio formats 🎵
- Enhanced error handling for specific cases 🛡️
- Optimizing Selenium performance ⚡

## 📧 Contact
Have questions or ideas? Reach out to me at **chedychaaben@gmail.com** 📬

## 📜 License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details. 📄