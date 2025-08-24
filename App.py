import customtkinter as ctk 
import time
from Components.HeaderFrame import HeaderFrame
from Components.HistoryFrame import HistoryFrame
from Components.BodyFrame import BodyFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.title("APIER")
        self.attributes("-fullscreen",True)
        #self.iconbitmap("12445912.ico")

        self.grid_columnconfigure((1),weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.header_frame = HeaderFrame(self)
        self.header_frame.grid(row=0,column=0,columnspan=2, sticky="ew")

        self.history_frame = HistoryFrame(self)
        self.history_frame.grid(row=1,column=0,sticky="wsn",pady=(5,5),padx=(5,5))

        self.body_frame = BodyFrame(self)
        self.body_frame.grid(row=1,column=1,sticky="nsew",pady=(5,5),padx=(5,5))
        self.state("normal")

    def zooms(self):
        self.iconify()

app = App()
app.mainloop()

        