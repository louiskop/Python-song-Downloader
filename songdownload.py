
from __future__ import unicode_literals
import youtube_dl
import os

# Download data and config

download_options = {
                'format':'bestaudio/best',
                'outtmpl':'%(title)s.%(ext)s',
                'nocheckcertificate':True,
                'postprocessors':[{
                    'key':'FFmpegExtractAudio',
                    'preferredcodec':'mp3',
                    'preferredquality':'192',
                }]
}

#song directory
if not os.path.exists('Songs'):
    os.mkdir('Songs')
    os.chdir('Songs')

else:
    os.chdir('Songs')

#download the songs

with youtube_dl.YoutubeDL(download_options) as dl:
    with open('../' + 'songlist.txt','r+') as f:
        for song_url in f:
            dl.download([song_url])
        f.truncate(0)

