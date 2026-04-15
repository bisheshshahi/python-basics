import requests
import io
import webbrowser
from tkinter import *
from urllib.request import urlopen, Request
from PIL import ImageTk, Image

class NewsApp:

    def __init__(self):
        # fetch data
        self.data = requests.get("https://newsapi.org/v2/everything?q=Nepal&language=en&apiKey=b44a32d740d44cff9a781986a84d0abf").json()

        # initial gui
        self.load_gui()

        # load the 1st news item
        self.load_news_item(0)

        self.root.mainloop()

    def load_gui(self):
        self.root = Tk()
        self.root.geometry("350x600")
        self.root.resizable(0, 0)
        self.root.config(background="black")

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index):
        self.clear()

        # Image
        image_url = self.data["articles"][index]["urlToImage"]

        try:
            req = Request(image_url, headers={"User-Agent": "Mozilla/5.0"})
            raw_data = urlopen(req).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)
            label = Label(self.root, image=photo)
            label.image = photo  # prevent garbage collection
            label.pack()

        except Exception:
            placeholder = Label(self.root, text="[Image not available]", bg="gray", fg="white", width=50, height=10)
            placeholder.pack()

        # Display title
        heading = Label(self.root, text=self.data["articles"][index]["title"], bg="black", fg="white", wraplength=350, justify="center")
        heading.pack(pady=(10, 20))
        heading.config(font=("verdana", 15))

        # Display description
        details = Label(self.root, text=self.data["articles"][index]["description"], bg="black", fg="white", wraplength=350, justify="center")
        details.pack(pady=(10, 20))
        details.config(font=("verdana", 12))

        # Buttons
        frame = Frame(self.root, bg="black")
        frame.pack(expand=True, fill=BOTH)

        # Btn1
        if index != 0: 
          prev_btn = Button(frame, text="Prev", width=16, height=3,
                            command=lambda: self.load_news_item(index - 1))
          prev_btn.pack(side=LEFT)

        # Btn2
        read_btn = Button(frame, text="Read more", width=16, height=3,
                          command=lambda: self.open_link(self.data["articles"][index]["url"]))
        read_btn.pack(side=LEFT)

        # Btn3
        if index != len(self.data["articles"])-1:
          next_btn = Button(frame, text="Next", width=16, height=3,
                            command=lambda: self.load_news_item(index + 1))
          next_btn.pack(side=LEFT)

    def open_link(self, url):
        webbrowser.open(url)

obj1 = NewsApp()