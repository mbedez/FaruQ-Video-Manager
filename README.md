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
- **Split** => Split a video in **n** parts. **{videoName} - part1** and **{videoName} - part2**
- **Merge** => Merge **n** videos together. **{firstVideoName}\_+_{secondVideoName}**
- **Accelerate** => Accelerate a video by the factors you input.  
  For example, if you input '**16,60,120**', you will create **{videoName}_x16**, **{videoName}_x60** and **{videoName}_x120**
***
## What do you need in order to set FaruQ Video Manager up?
FaruQ Video Manager runs in python with the help of the **moviepy** package. In order to run the soft, you will need a few things :
- python (*of course*)
- moviepy : A library used to do differents modification on a video file

You have to **edit the iconPath in the python file** by changing it with his absolute path. (example : "C:\\Users\\UserName\\Documents\\icon.ico")  
But if you absolutly don't care about my beautiful icon you can remove it and remove the lines where "iconPath" appears too.  

You can also use `pip install -r requirements.txt` to install the necessary libraries.
***
## How to run FaruQ Video Manager
Simply run the python file or his shortcut with python or do from the terminal.  
For example with the command `python FaruQVideoManager.py`
***
# Notes
Even if the program **is not responding** it's actually running well in background, you can see what it's really doing in the console if you run it with an IDE or with python without the terminal.
