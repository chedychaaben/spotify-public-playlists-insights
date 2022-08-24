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

def download_vid_with_pytube(video_url):
    yt = pt.YouTube(video_url)
    t = yt.streams.filter(only_audio=True)
    
    # download the file
    out_file = t[0].download()

    # save the file as mp3
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)