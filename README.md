# youtubeDownloader
script to download either video or audio of a youtube video


`````````````````````````````````````````````````````````````````````````````````````````````
Update 4/4/2021:
-Changed how bot gets youtube stream for download
-Now downloads videos with the audio
-Makes .mp3 file for audio only

Used to rely on youtube videos having certain streams, then
would either download video with no audio, or audio as .mp4.
Now it downloads the highest quality stream with video and 
audio, and audio only is converted from .mp4 to .mp3.

`````````````````````````````````````````````````````````````````````````````````````````````
`````````````````````````````````````````````````````````````````````````````````````````````
Update 10/24/2021:
-Changed how bot converts/downloads mp3's

The bot used to download .mp3 files by first downloading a
.mp4 file and then changing the extension to .mp3. While this
technically worked, this was not a great solution and could not 
use the .mp3's elsewhere. Now the bot goes through a different 
process to download .mp3 files that are more usable

`````````````````````````````````````````````````````````````````````````````````````````````
`````````````````````````````````````````````````````````````````````````````````````````````
Update 1/29/202:
-Created GUI .mp3 converter

There is now an easier way to download YouTube videos to the 
desktop as .mp3's. With this new GUI, you can input the YouTube
URL and press the download button. After a few moments, a message
will appear stating that the .mp3 was downloaded successfully. No 
more command line interface.

`````````````````````````````````````````````````````````````````````````````````````````````
