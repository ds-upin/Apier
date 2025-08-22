import customtkinter as ctk
from .RequestFrame import RequestFrame
from .ResponseFrame import ResponseFrame

class BodyFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.grid_rowconfigure((0,),weight=2)
        self.grid_rowconfigure((1),weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.request_frame = RequestFrame(self)
        self.request_frame.grid(row=0,column=0,padx=(5,5),pady=(5,5),sticky="nsew")

        self.response_frame = ResponseFrame(self)
        self.response_frame.grid(row=1,column=0,padx=(5,5),pady=(5,5),sticky="nsew")

