import tkinter as tk
from tkinter import *
from tkinter import ttk

import youtube_dl

root = tk.Tk()
root.geometry('300x300')
root.resizable(False, False)
root.title('YouTube 2 MP3')


def converter():
    msgSent.delete('1.0', END)
    msgSent.insert(INSERT, "Please Wait, May Take a Moment")
    msgSent.update()

    video_url = url.get()
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )

    filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename
    }

    try:
        with youtube_dl.YoutubeDL(options) as ydl:
            print("Attempting download... \n")
            ydl.download([video_info['webpage_url']])
        msgSent.delete('1.0', END)
        msgSent.insert(INSERT, f"Sussessfully downloaded {filename}")
        msgSent.update()
    except Exception as e:
        print("Fatal Error Occurred! Code: " + e)
    pass


url = tk.StringVar()
frameURL = LabelFrame(root, text='URL')
frameURL.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
frameURL.place(
    x=85,
    y=65
)
Entry(frameURL, textvariable=url).pack()


submit = ttk.Button(
    root,
    text="Download",
    command=lambda: converter()
)
submit.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
submit.place(
    x=115,
    y=130
)

msgSent = tk.Text(root, width=30, height=2)
msgSent.place(
    x=30,
    y=175
)

if __name__ == '__main__':
    root.mainloop()
