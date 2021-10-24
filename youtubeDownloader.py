import pytube
import os
import time


def video(link):
    print("Starting...")
    video = pytube.YouTube(link)
    stream = video.streams.get_highest_resolution()
    stream.download()
    print("Finished!")
    time.sleep(.5)
    os.system('cls')


def audio(link):
    print("Starting...")
    
    video_url = link
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )

    filename = f"{video_info['title']}.mp3"
    options={
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename
    }

    try:
        with youtube_dl.YoutubeDL(options) as ydl:
            print("Attempting download... \n")
            ydl.download([video_info['webpage_url']])
    except Exception as e:
        print("Fatal Error Occurred! Code: " + e)

    print("Finished!")
    time.sleep(.5)
    os.system('cls')


def main():
    print("Welcome to the youtube downloader")
    print()

    while True:
        print("1. Video\n"
              "2. Audio\n"
              "3. Exit")
        print()
        choice = int(input("What would you like to do? "))

        if choice == 1:
            url = input("Enter url: ")
            video(url)
        elif choice == 2:
            url = input("Enter url: ")
            audio(url)
        elif choice == 3:
            print("Goodbye")
            break
        else:
            print("Enter Number 1-3")


main()
