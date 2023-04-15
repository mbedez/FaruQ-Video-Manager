# FaruQ Video Manager
***
[Intro](#What-is-FaruQ-Video-Manager) - [Functionality](#What-can-you-do-with-it) - [Setup](#What-do-you-need-in-order-to-set-FaruQ-Video-Manager-up) - [Run](#How-to-run-FaruQ-Video-Manager) - [Extra](#Notes)
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
***
## What do you need in order to set FaruQ Video Manager up?
FaruQ Video Manager runs in python with the help of the **moviepy** package. In order to run the soft, you will need a few things :
- python (*of course*)
- moviepy : A library used to do differents modification on a video file

You have to **edit the line 10 of the python file** by changing the path with the absolute path of the icon.  
But if you absolutly don't care about my beautiful icon you can remove it and remove the line 10 too.  

You can also use `pip install -r requirements.txt` to install the necessary libraries.
***
## How to run FaruQ Video Manager
Simply run the python file or his shortcut with python or do from the terminal.  
For example with the command `python FaruQVideoManager.py`
***
# Notes
Even if the program **is not responding** it's actually running well in background, you can see what it's really doing in the console if you run it with an IDE or with python without the terminal.
