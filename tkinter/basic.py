from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def handle_login():
  email = email_input.get()
  password = password_input.get()
  
  if email == "bisheshshahi13@gmail.com" and password == "1234":
    messagebox.showinfo("Congratulation","Login successfull")
  
  else:
    messagebox.showerror("Error","Login failed")

#root is the object of Tk class
root = Tk()

root.title('Login Form')

root.iconbitmap('D:/bishesh/python-basics/gui/bishesh_icon.ico')

img = Image.open('D:/bishesh/python-basics/gui/flipkart_logo.png')
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)

#label is generally used for priting text, but you can also print image
img_label = Label(root,image = img)

#Whenever you create label you should explicitly place in gui, need geometry manager
img_label.pack(pady=(10,10))

# root.minsize(200,300)

# for particular size
root.geometry('300x400')

#configure = function, background = attribute, flipkart background
root.configure(background="#0096DC")

text_label = Label(root, text="FlipKart", fg="white", bg="#0096DC")
text_label.pack()
text_label.config(font=("verdana",24))

email_label = Label(root, text="Enter email:", fg="white", bg="#0096DC")
email_label.pack(pady=(20,5))
email_label.config(font=("verdana",10))

email_input = Entry(root, width=50)
email_input.pack(ipady=4, pady=(1,15))

password_label = Label(root, text="Enter password:", fg="white", bg="#0096DC")
password_label.pack(pady=(20,5))
password_label.config(font=("verdana",10))

password_input = Entry(root,show="*", width=50)
password_input.pack(ipady=4, pady=(1,15))
  
login_btn = Button(root,text="Login", bg= "white", fg = "black", width = 20, height = 2, command = handle_login)
login_btn.pack(pady = (10,20))
login_btn.config(font=("verdana",10))


#mainloop consistently shows gui on main screen
#if we do not add this line then gui will show up and go away so fast that we'll not even know
root.mainloop()