import pytube


def video(link):
    print("Starting...")
    video = pytube.YouTube(link)
    stream = video.streams.get_by_itag(299)
    stream.download()
    print("Finished!")


def audio(link):
    print("Starting...")
    video = pytube.YouTube(link)
    stream = video.streams.get_by_itag(140)
    stream.download()
    print("Finished!")


def main():
    print("Welcome to the youtube downloader")
    print()

    while True:
        print("1. Video (No Audio)\n"
              "2. Audio (No Video)\n"
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
