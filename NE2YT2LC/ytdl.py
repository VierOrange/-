from __future__ import unicode_literals
from pickle import TRUE
import yt_dlp
import os 
import opencc


pt_path = "./pt.txt"

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
        pass


def my_hook(d):
    if d['status'] == 'downloading':
        try:
            print("\r",f"Downloading {d['filename'][7:]} to ./{d['filename'][:6]} at {(d['speed']/1000000):.2f} MiB/s ...", end="")
        except:
            print("\r",f"Downloading ...", end="")
    if d['status'] == 'finished':
        print('\nDone downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
    'noplaylist':True,
    'default_search':'auto',
    'paths':{'home':"./rsongs"},
    'max_filesize':128000000,


}

def check_song(song,songs):
    converter = opencc.OpenCC('t2s.json')
    song = song.lower()
    for s in songs:
        if song in converter.convert(s.lower()):
            return True
    return False

def main():

    dled_songs = os.listdir("./songs")+os.listdir("./rsongs")
    dl_songs =[]

    with open(pt_path,encoding="utf-8") as f: 
        songs = f.readlines()
    
    for idx,song in enumerate(songs):
        songs[idx] = song.replace("\xa0"," ").replace("\n"," ").strip()
    
    for song in songs:
        if not check_song(song,dled_songs):
            dl_songs.append(song)
            

    print(len(dl_songs))
    #print(dl_songs)

    # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    #     for song in songs:
    #         if not check_song(song,dled_songs):
    #             try:
    #                 ydl.download(song)
    #             except:
    #                 pass

if __name__ == "__main__":
    main()