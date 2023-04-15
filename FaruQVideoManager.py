import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog
import os

# Create a tkinter window and a "Browse" button
root = tk.Tk()
root.title('FaruQ Video Manager')
# change the path bellow by your path of the icon file 
root.iconbitmap("C:\\Users\\Username\\icon.ico")
root.geometry("425x100")
button1 = tk.Button(text="Splitter une vidéo", command=lambda: select_file(1))
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = tk.Button(text="Fusionner deux vidéos", command=lambda: select_file(2))
button2.grid(row=0, column=1, padx=10, pady=10)

button3 = tk.Button(text="Accélerer une vidéo", command=lambda: select_file(3))
button3.grid(row=0, column=2, padx=10, pady=10)

output = tk.Text(root, height=2, width=50)
output.grid(row=1, column=0, columnspan=3, padx=10)

output.configure(state="normal")
output.delete('1.0', 'end')
output.insert(tk.END, "Welcome to FaruQ Video Manager\nPlease select an option")
output.configure(state="disabled")


def select_file(choice, merge_file_path=None):
  # Open a file selection dialog and get the selected file's path
  file_path = filedialog.askopenfilename()
  # Change the working directory to the file's directory
  os.chdir(os.path.dirname(file_path))
  if choice == 1:
    split_video(file_path)
  elif choice == 2:
    select_file(4, file_path)
  elif choice == 3:
    accelerate_video(file_path)
  elif choice == 4:
    merge_video(merge_file_path, file_path)
  else:
    print("Error")

def split_video(file_path):

  file_name = os.path.basename(file_path).split('/')[-1]
  file_name, file_ext = file_name.rsplit(".", 1)

  editText(f"Splitting {file_name}.{file_ext} ...")

  # Use moviepy to split the video into two files at the halfway point
  clip = mp.VideoFileClip(file_path)

  duration = clip.duration
  halfway_point = duration / 2
  clip1 = clip.subclip(0, halfway_point)
  clip2 = clip.subclip(halfway_point, duration)
  
  clip1.write_videofile(f"{file_name} - part1.{file_ext}")
  clip2.write_videofile(f"{file_name} - part2.{file_ext}")

  editText(f"Done !\nPlease select an option")

def accelerate_video(file_path):

  # Extract the file name and extension from the input video path
  file_name = os.path.basename(file_path).split('/')[-1]
  file_name, file_ext = file_name.rsplit(".", 1)

  print("File name :",file_name)
  print("File extension :",file_ext)
  editText(f"Accelerating {file_name}.{file_ext} ...")

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

  editText(f"Done !\nPlease select an option")

def merge_video(first_file_path, second_file_path):
    
  # Extract the file names and extensions from the input video paths
  first_file_name = os.path.basename(first_file_path).split('/')[-1]
  first_file_name, first_file_ext = first_file_name.rsplit(".", 1)

  second_file_name = os.path.basename(second_file_path).split('/')[-1]
  second_file_name, second_file_ext = second_file_name.rsplit(".", 1)

  # Generate the output file name
  output_video = f"{first_file_name}_and_{second_file_name}.{first_file_ext}"

  editText(f"Merging {first_file_name}.{first_file_ext} and {second_file_name}.{second_file_ext} ...")

  # Merge the videos
  first_clip = mp.VideoFileClip(first_file_path)
  second_clip = mp.VideoFileClip(second_file_path)
  merged_clip = mp.concatenate_videoclips([first_clip, second_clip])
  merged_clip.write_videofile(output_video)

  editText(f"Done !\nPlease select an option")


def editText(text):
  output.configure(state="normal")
  output.delete('1.0', 'end')
  output.insert(tk.END, text)
  output.configure(state="disabled")
  root.update()

# Run the tkinter event loop
root.mainloop()