from tkinter import *
from PIL import ImageTk, Image
import os

def wallpaper_viewer():
  global counter
  img_label.config(image = img_list[counter%len(img_list)])
  counter += 1

counter = 1
root = Tk()
root.title("Wallpaper Viewer")

root.geometry("250x300")
root.configure(background = "black")

folder = os.path.dirname(__file__)
subfolder = os.path.join(folder, "wallpapers")
files = os.listdir(subfolder)

img_list = []

for file in files:
  img = Image.open(os.path.join(subfolder,file))
  resized_img = img.resize((150,200))
  img_list.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root, image = img_list[0])
img_label.pack(pady=(15,10))

label_btn = Button(root, text = "Next", width = 20, command = wallpaper_viewer)
label_btn.pack()

root.mainloop()