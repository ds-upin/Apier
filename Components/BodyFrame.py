import customtkinter as ctk
from threading import Thread
from .RequestFrame import RequestFrame
from .ResponseFrame import ResponseFrame
from .Services.HttpClient import HttpClient

class BodyFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.master=master
        self.data = dict()
        self.response=None
        self.thread = None
        self.grid_rowconfigure((0,),weight=2)
        self.grid_rowconfigure((1),weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.request_frame = RequestFrame(self,callback=self.callback)
        self.request_frame.grid(row=0,column=0,padx=(5,5),pady=(5,5),sticky="nsew")

        self.response_frame = ResponseFrame(self)
        self.response_frame.grid(row=1,column=0,padx=(5,5),pady=(5,5),sticky="nsew")

     
    def callback(self,data):
        self.data=data
        def send_request_thread():
            try:
                print(self.data)
                response = HttpClient(payload=self.data).send_request()
                print("Response Recived",response.status_code)
            except Exception as e:
                print("Exception occured",e)

        self.thread = Thread(target=send_request_thread)
        self.thread.daemon = True
        self.thread.start()
        self.check_thread_alive()

    def check_thread_alive(self):
        if self.thread.is_alive:
            #print("waiting for response")
            self.master.after(100,self.check_thread_alive)
        else:
            print("Finished",self.response)
