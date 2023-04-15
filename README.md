# FaruQ Video Manager
***
[Intro](#What-is-FaruQ-Video-Manager) - [Commands](#What-can-you-do-with-it) - [Setup](#What-do-you-need-in-order-to-set-FafBot-up)
***
## What is FaruQ Video Manager?
FaruQ Video Manager is a small project I made for a someone to speed, split in two, or merge video(s).
This software is designed to run on Win10.
***
## What can you do with it?
Here's a list of different things you could do with this soft:
- **Split** => Split one video in two parts. **{videoName} - part1** and **{videoName} - part1**
- **Merge** => Merge two videos together. **{firstVideoName}_and_{secondVideoName}**
- **Accelerate** => Accelerate a video by x16, x60 and x120. **{videoName}_x16**, **{videoName}_x60** and **{videoName}_x120**
  If you provided an int, the returned number will be between 1 and the int. It must be less or equal to 6.

***
## What do you need in order to set FaruQ Video Manager up?
FaruQ Video Manager runs in python with the help of the **moviepy** package. In order to run the soft, you will need a few things :
- python3 (*of course*)
- moviepy : A library used to do differents modification on a video file

You can also use `pip install -r requirements.txt` to install the necessary libraries.
