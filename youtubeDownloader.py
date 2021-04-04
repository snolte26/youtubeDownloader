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
    video = pytube.YouTube(link)
    stream = video.streams.get_audio_only()
    stream.download()

    try:
        files = os.listdir(os.curdir)
        for file in files:
            if '.mp4' in file:
                newfile = file.replace('.mp4', '.mp3')
                os.rename(file, newfile)
    except:
        print("Couldn't convert MP4 to MP3, "
              "Please do so manually")
        pass

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
