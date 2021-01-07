from pytube import YouTube
from pytube import Playlist
#from pytube import exceptions

import os 
import sys
#import shutil

from moviepy import editor

previousprogress = 0

def on_progress(stream, chunk, bytes_remaining):
    global previousprogress
    # total_size = stream.filesize
    # bytes_downloaded = total_size - bytes_remaining 

    # liveprogress = (int)(bytes_downloaded / total_size * 100)
    # if liveprogress > previousprogress:
    #     previousprogress = liveprogress
    #     print(liveprogress, '% done...')

    liveprogress = ((stream.filesize - bytes_remaining)/stream.filesize)
    percent = ('{0:.1f}').format(liveprogress*100)
    progress = int(50*liveprogress)

    if liveprogress > previousprogress:
        previousprogress = liveprogress
        status = '█' * progress + '-' * (50 - progress)
        sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
        sys.stdout.flush()
    else:
        previousprogress = 0 #IF END, RESET THE GLOBAL VAR

def fix_title(title):
    title = title.replace(",", " ")     \
                .replace(";", " ")      \
                .replace(" | ", " ")    \
                .replace("|", "")       \
                .replace(" / ", " ")    \
                .replace("/", "")       \
                .replace(" \ ", " ")    \
                .replace("\\", "")      \
                .replace(".", " ")      \
                .replace(":", " ")      \
                .replace("  ", " ")     \
                .replace("'", "")       \
                .replace('"', '')       \
                .replace("#", "")       \
                .replace("$", "")       \
                .replace("?", "")
    return title

class download():
    def __init__(self, url, dwn_type):
        self.url = url
        self.dwn_type = dwn_type
        self.yt = YouTube(self.url)
        self.yt.register_on_progress_callback(on_progress)
        self.title = self.yt.title
        
        self.title = fix_title(self.title)
    
        global previousprogress

        # if self.dwn_type != 3:
        #     print(f"\nFILE: {self.title}\n")
      
    def downld(self):
        # Audio
        if self.dwn_type == 1:   
            #print("DOWNLOADING")
            print("\nDOWNLOADING FILE: {}".format(self.title))
            #self.yt.streams.filter(mime_type="audio/mp4", only_audio=True).first().download('/home/voalle/Music',filename=self.title) #filename_prefix
            self.yt.streams.filter().first().download('/home/voalle/Music',filename=self.title) #filename_prefix

            mp4 = f"/home/voalle/Music/{self.title}.mp4"
            mp3 = f"/home/voalle/Music/{self.title}.mp3"

            #os.rename(mp4,mp3)

            video_conv = editor.VideoFileClip(os.path.join(mp4))

            editor.audio_conv = video_conv.audio

            editor.audio_conv.write_audiofile(mp3, logger=None)
            
            editor.audio_conv.close()

            os.remove(mp4)

            video_conv.close()

        # Video
        elif self.dwn_type == 2:
            #self.chres = input("\nTYPE THE RESOLUTION:\n>")
            self.chres = '360p' 
            #print("DOWNLOADED")
            print("\nDOWNLOADING FILE: {}".format(self.title))
            self.yt.streams.filter(res=self.chres).first().download('/home/voalle/Music')
            
        # Playlist
        elif self.dwn_type == 3:
            #self.chres = input("\nTYPE THE RESOLUTION:\n>") 
            #self.chres = '360p'
           
            self.pl = Playlist(self.url)

            try: 
                for video in self.pl.videos: 
                    video.register_on_progress_callback(on_progress)
            
                    self.title = fix_title(video.title)

                    print("\nDOWNLOADING FILE: {}".format(video.title))
                    #print("DOWNLOADED")
                    #video.streams.filter(res=self.chres).first().download('/home/voalle/Music')      
                    video.streams.filter().first().download('/home/voalle/Music',filename=self.title) #filename_prefix

                    print('\n')

                    mp4 = f"/home/voalle/Music/{self.title}.mp4"
                    mp3 = f"/home/voalle/Music/{self.title}.mp3"

                    #os.rename(mp4,mp3)

                    video_conv = editor.VideoFileClip(os.path.join(mp4))

                    editor.audio_conv = video_conv.audio

                    editor.audio_conv.write_audiofile(mp3, logger=None)
                    
                    editor.audio_conv.close()

                    os.remove(mp4)

                    video_conv.close()
            except:  
                print("\nTHIS PLAYLIST HAVE INVALID VIDEOS\nPLEASE, INSERT A VALID PLAYLIST!\n")   
        
        return None

if __name__ == '__main__':

    """
        TODO:
            VIDEO PLAYLIST OR AUDIO PLAYLIST 
            FUNÇÃO DE REPLACE GERAL
            CLASSE PARA CADA TIPO (MUSICA, VIDEO, PLAYLIST)
    """
    ret = None 
    
    while ret is None:
       
        dwn_type = int(input("\n\nTYPE OF DOWNLOADS AVALIABLE:\n[1 - Audio]\n[2 - Video]\n[3 - Playlist]\n[99 - Exit]\nCHOICE:\n>")) #download type

        if dwn_type == 99:
            print("\nBYE BYE BABY ;*")
            exit(1)

        url = input("\nPASTE THE URL BELOW:\n>") #url to download

        # d = download(url,dwn_type)
        
        # ret = d.downld()
        ret = download(url,dwn_type).downld()

   