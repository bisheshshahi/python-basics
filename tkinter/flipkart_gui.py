from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
  email = email_input.get()
  password = password_input.get()

  if email != "" and password != "":
    if email == "test@gmail.com" and password == "1234":
      messagebox.showinfo("Congratulations", "Login Successful")
    
    else:
      messagebox.showerror("Error", "Login failed")
  else:
    messagebox.showerror("Error", "Please fill both fields")

root = Tk()
root.title("Login")
root.minsize(275,340)

root.configure(background = "#0096DC")

root.iconbitmap("D:/bishesh/python-basics/tkinter/bishesh_icon.ico")
img = Image.open("D:/bishesh/python-basics/tkinter/flipkart.png")
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root, image= img)
img_label.pack(pady = (10,5))

email_label = Label(root, text = "Enter your email:", fg = "white", bg = "#0096DC", font = "verdana")
email_label.pack(pady=(20,10))

email_input = Entry(root, width = 50)
email_input.pack(ipady=5,pady=5)

password_label = Label(root, text="Enter your password:",fg = "white", bg = "#0096DC", font = "verdana")
password_label.pack(pady = (20,10))

password_input = Entry(root, width = 50, show = "*" ) 
password_input.pack(ipady=5, pady=5)

login_btn = Button(root, text = "Login", width = 15, height = 2, font = "verdana", command = handle_login)
login_btn.pack(pady = (10,5))

root.bind("<Return>", lambda event: handle_login())

root.mainloop()