import os
import yt_dlp
import pytube as pt

def download_vid_with_yt_dlp(video_url, folder_name):
    try:
        video_info = yt_dlp.YoutubeDL().extract_info(url=video_url, download=False)
        filename = f"{video_info['title']}.mp3"
        output_path = os.path.join(os.getcwd(), folder_name)
        os.makedirs(output_path, exist_ok=True)
        options = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, filename),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([video_url])
        print(f"Download complete: {filename}")
        return os.path.join(output_path, filename)
    except Exception as e:
        print(f"Error downloading with yt_dlp: {e}")
        return None

def download_vid_with_pytube(video_url, folder_name):
    try:
        yt = pt.YouTube(video_url)
        stream = yt.streams.filter(only_audio=True, abr="160kbps").first() or \
                 yt.streams.filter(only_audio=True).first()
        if not stream:
            raise ValueError("No suitable audio stream found")
        safe_title = "".join(c for c in yt.title if c not in r'\/:*?<>|')
        output_path = os.path.join(os.getcwd(), folder_name)
        os.makedirs(output_path, exist_ok=True)
        created_file = stream.download(output_path=output_path, filename=safe_title)
        print(f"Download complete: {created_file}")
        return created_file
    except Exception as e:
        print(f"Error downloading with pytube: {e}")
        return None