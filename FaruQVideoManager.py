import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import os

iconPath = "icon.ico"

class window():
  def __init__(self):
    # Create a tkinter window and a "Browse" button
    self.root = tk.Tk()
    self.root.title('FaruQ Video Manager')
    # change the path bellow by your path of the icon file 
    self.root.iconbitmap(default=iconPath)
    self.root.resizable(width=False, height=False)
    self.root.geometry("425x100")
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
    pass

  def select_file(self, choice, merge_file_path=None):
    if choice == 1: # split  
      file_path = filedialog.askopenfilename()
      os.chdir(os.path.dirname(file_path))
      value = self.getValue(1)
      if value != None : self.split_video(file_path, value)
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
      self.accelerate_video(file_path)
    else:
      print("Error")    

  def split_video(self, file_path, n):

    file_name = os.path.basename(file_path).split('/')[-1]
    file_name, file_ext = file_name.rsplit(".", 1)

    self.editText(f"Splitting {file_name}.{file_ext} ...")

    # Use moviepy to split the video into two files at the halfway point
    clip = mp.VideoFileClip(file_path)
    duration = clip.duration

    clips = []
    for i in range(n):
      clips.append(clip.subclip(i*duration/n, (i+1)*duration/n))
      
    for i, clip in enumerate(clips):
      clip.write_videofile(f"{file_name} - part{i+1}.{file_ext}")

    self.editText(f"Done !\nPlease select an option")

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

    self.editText(f"Done !\nPlease select an option")

  def accelerate_video(self, file_path):

    # Extract the file name and extension from the input video path
    file_name = os.path.basename(file_path).split('/')[-1]
    file_name, file_ext = file_name.rsplit(".", 1)

    self.editText(f"Accelerating {file_name}.{file_ext} ...")

    # Generate the output file names
    output_videos = []
    factors = [16, 60, 120]

    for factor in factors:
        output_video = f"{file_name}_x{factor}&Time.{file_ext}"
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
