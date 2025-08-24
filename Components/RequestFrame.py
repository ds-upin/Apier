import customtkinter as ctk 
from .TabFrame import TabFrame

class RequestFrame(ctk.CTkFrame):
    def __init__(self,master,callback,start_progress_callback):
        super().__init__(master)
        self.callback = callback
        self.start_progress_callback = start_progress_callback
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        

        self.tab_body = TabFrame(self,self.callback,self.start_progress_callback1)
        self.tab_body.grid(row=1,column=0,padx=(5,5),pady=(5,5),sticky="nsew")

    def enable_button(self):
        self.tab_body.enable_button()

    def on_tab_button(self,btn):
        btn.configure(fg_color=("blue"))

    def get_data_for_request(self):
        data =  self.tab_body.get_all_data()
        self.callback(data)
    def start_progress_callback1(self):
        self.start_progress_callback()


