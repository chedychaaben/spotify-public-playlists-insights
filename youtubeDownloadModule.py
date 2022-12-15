import os
import youtube_dl
import pytube as pt

def download_vid_with_youtube_ld(video_url):
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))

def download_vid_with_pytube(video_url, folder_name):
    yt = pt.YouTube(video_url)

    out_file = yt.streams.filter(abr="160kbps", progressive=False).first()#get_audio_only()
    
    filename_to_make = "".join(i for i in out_file.title if i not in "\/:*?<>|") #+ ".mp3"

    created_file = out_file.download(output_path = os.getcwd() + '\\' + folder_name, filename=filename_to_make)
    # Converting the webm to mp3