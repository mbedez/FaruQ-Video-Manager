import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import os
import sys

# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



iconPath = resource_path(".\\icon.ico")

class window():
  def __init__(self):
    # Create a tkinter window and a "Browse" button
    self.root = tk.Tk()
    self.root.title('FaruQ Video Manager')
    # change the path bellow by your path of the icon file 
    self.root.iconbitmap(default=iconPath)
    self.root.resizable(width=False, height=False)
    self.root.geometry("375x100")
    button1 = tk.Button(text="Split a video", command=lambda: self.select_file(1))
    button1.grid(row=0, column=0, padx=10, pady=10)

    button2 = tk.Button(text="Merge videos together", command=lambda: self.select_file(2))
    button2.grid(row=0, column=1, padx=10, pady=10)

    button3 = tk.Button(text="Accelerate a video", command=lambda: self.select_file(3))
    button3.grid(row=0, column=2, padx=10, pady=10)

    self.output = tk.Text(self.root, height=2, width=50)
    self.output.grid(row=1, column=0, columnspan=3, padx=10)

    self.output.configure(state="normal", font=("Arial", 10))
    self.output.delete('1.0', 'end')
    self.output.insert(tk.END, "Welcome to FaruQ Video Manager!\nPlease select an option!")
    self.output.configure(state="disabled")

    # Run the tkinter event loop
    self.root.mainloop()

  def getValue(self, choice):
    if choice == 1 or choice == 2:
      if choice == 1: prompt="How many parts du you want to split the video into?"
      elif choice == 2: prompt="How many parts du you want to merge into?"

      value = simpledialog.askinteger(title="", prompt=prompt,  initialvalue=2, minvalue=2, maxvalue=10)
      if value != None:
        return value
    elif choice == 3:
      value = simpledialog.askinteger(title="", prompt="Type 1 for regular split or type 2 for custom split!",  initialvalue=1, minvalue=1, maxvalue=2)
      if value != None and value == 1:
        return value
      elif value != None and value == 2:
        return simpledialog.askstring(title="", prompt="Give your timecode in seconds! (example : '60,120,121')")
    elif choice == 4:
      return simpledialog.askstring(title="", prompt="Give your factors! (example : '1.5,2,120')")
    pass

  def select_file(self, choice):
    if choice == 1: # split  
      file_path = filedialog.askopenfilename()
      os.chdir(os.path.dirname(file_path))
      value = self.getValue(3)
      if value != None and value == 1: # regular split
        value = self.getValue(1)
        if value != None : self.regularSplit(file_path, value)
      else: self.customSplit(file_path, value)# custom split
    elif choice == 2: # merge
      mergelist = []
      value = self.getValue(2)
      if value != None :
        file_path = filedialog.askopenfilename()
        os.chdir(os.path.dirname(file_path))
        mergelist.append(file_path)
        for _i in range(value-1):
          file_path = filedialog.askopenfilename()
          mergelist.append(file_path)
        self.merge_video(mergelist)
    elif choice == 3: # accelerate
      file_path = filedialog.askopenfilename()
      os.chdir(os.path.dirname(file_path))
      value = self.getValue(4)
      if value != None : self.accelerate_video(file_path, value) 

  def regularSplit(self, file_path, n):

    clip = mp.VideoFileClip(file_path)
    
    timeList = []
    for i in range(n):
      timeList.append(i*clip.duration/n)
    timeList.append(clip.duration)
    self.split_video(file_path, timeList, clip)

  def customSplit(self, file_path, timeString):

    clip = mp.VideoFileClip(file_path)
    
    timeList = timeString.split(',')
    nombresValides=True 

    for i in range(len(timeList)):
      timeList[i] = str(timeList[i])

      if timeList[i].replace('.',"1").isnumeric() == True:
        if int(float(timeList[i])) <= 0 and int(float(timeList[i])) >= clip.duration:
          clip = None
          nombresValides=False
      else: clip = None
    
    if nombresValides == True:
      for i in range(len(timeList)):
        timeList[i] = int(float(timeList[i]))
      timeList.insert(0, 0)
      timeList.append(clip.duration)
      if sorted(timeList) != timeList:
        clip = None

    if clip == None:
      self.editText("Error!\nPlease select an option!")
    else:
      self.split_video(file_path, timeList, clip)

  def split_video(self, file_path, timeList, clip):

    file_name = os.path.basename(file_path).split('/')[-1]
    file_name, file_ext = file_name.rsplit(".", 1)

    runningPrompt = f"Splitting {file_name} in {len(timeList)-1} parts..."
    self.editText(runningPrompt)

    clips = []
    for i in range(len(timeList)-1):
      clips.append(clip.subclip(timeList[i], timeList[i+1]))
      
    for i, clip in enumerate(clips):
      clip.write_videofile(f"{file_name} - part{i+1}.{file_ext}")

    self.editText(f"Done!\nPlease select an option!")

  def merge_video(self, mergelist):
      
    file_name_list = []
    file_ext_list = []
    for i in range(len(mergelist)):
      file_name = os.path.basename(mergelist[i]).split('/')[-1]
      file_name, file_ext = file_name.rsplit(".", 1)
      file_name_list.append(file_name)
      file_ext_list.append(file_ext)

    # Generate the output file name
    output_video_name = f"{file_name_list[0]}"
    for i in range(len(mergelist)-1):
      output_video_name += f" + {file_name_list[i+1]}"
    output_video_name += f".{file_ext_list[0]}"

    runningPrompt = f"Merging {file_name_list[0]}.{file_ext_list[0]}"
    for i in range(len(mergelist)-1):
      runningPrompt += f" + {file_name_list[i+1]}.{file_ext_list[i+1]}"
    self.editText(f"{runningPrompt} ...")

    # Merge the videos
    clipList = []
    for i in range(len(mergelist)):
      clipList.append(mp.VideoFileClip(mergelist[i]))

    merged_clip = mp.concatenate_videoclips(clipList)
    merged_clip.write_videofile(output_video_name)

    self.editText(f"Done!\nPlease select an option!")

  def parseFactors(self, factors):
    factors = factors.split(',')
    for i in range(len(factors)):
      if factors[i].replace('.',"1").isnumeric() == True:
        if float(factors[i]) <= 0 and float(factors[i]) > 200:
          return None
      else:
        return None
    for i in range(len(factors)):
      factors[i] = float(factors[i])
    return factors

  def accelerate_video(self, file_path, factorsString):

    # Extract the file name and extension from the input video path
    file_name = os.path.basename(file_path).split('/')[-1]
    file_name, file_ext = file_name.rsplit(".", 1)

    self.editText(f"Accelerating {file_name}.{file_ext} ...")

    factors = self.parseFactors(factorsString)
    if factors == None:
      self.editText(f"Error!\nPlease select an option!")
      return

    # Generate the output file names
    output_videos = []

    for factor in factors:
        output_video = f"{file_name}_x{factor}.{file_ext}"
        output_videos.append(output_video)

    clip = mp.VideoFileClip(file_path)

    for output_video, factor in zip(output_videos, factors):
        # Accelerate the video
        accelerated_clip = clip.speedx(factor=factor)

        # save the output video
        accelerated_clip.write_videofile(output_video)

    self.editText(f"Done!\nPlease select an option!")

  def editText(self, text):
    self.output.configure(state="normal")
    self.output.delete('1.0', 'end')
    self.output.insert(tk.END, text)
    self.output.configure(state="disabled")
    self.root.update()

myApp = window()
