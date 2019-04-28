from __future__ import unicode_literals
import youtube_dl

VIDEO_LIST = []
FORM_LIST = []


def main():
    STOP = ''
    while STOP != 'y':
        v_url = input('Enter video URL you wish to download: ')
        form = input("Enter format ('audio' or 'video'): ")
        VIDEO_LIST.append(v_url)
        if form == 'audio'.lower():
            FORM_LIST.append('m4a')
        elif form == 'video'.lower():
            FORM_LIST.append('mp4')
        STOP = input("Exit? (Y/N): ").lower()

    i = 0
    while i < len(VIDEO_LIST):
        ydl_opts = {'format': FORM_LIST[i]}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([VIDEO_LIST[i]])
        i += 1


if __name__ == "__main__":
    main()
