import customtkinter as ctk 
from .TabFrame import TabFrame

class RequestFrame(ctk.CTkFrame):
    def __init__(self,master,callback):
        super().__init__(master)
        self.callback = callback
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        
        self.no_tabs = 1
        self.tabs = []
        self.tab_frame = ctk.CTkScrollableFrame(self,height=30,orientation="horizontal")
        self.tab_frame.grid(row=0,column=0,padx=(5,5),pady=(5,5),sticky="ew")

        for i in range(self.no_tabs):
            self.add_tab()
        self.tab = ctk.CTkButton(self.tab_frame,text="+",width=50,command=self.add_tab, fg_color=("orange","green"))
        self.tab.grid(row=0,column=1000)

        self.tab_body = TabFrame(self,self.callback)
        self.tab_body.grid(row=1,column=0,padx=(5,5),pady=(5,5),sticky="nsew")


    def add_tab(self):
        tab_index = self.no_tabs
        btn = ctk.CTkButton(self.tab_frame, width=70, text=f"Tab {tab_index}", fg_color="transparent")
        btn2 = ctk.CTkButton(self.tab_frame, width=20, text="x",command=lambda: self.remove_tab(btn,btn2) ,fg_color="transparent", hover_color=("red","red"))

        btn.grid(row=0, column=tab_index*2)
        btn2.grid(row=0, column=tab_index*2+1,padx=(0,5))
    
        self.no_tabs += 1
        self.tabs.append((btn, btn2))

    def remove_tab(self, btn, btn2):
        if (len(self.tabs)==1):
            return 
        btn.destroy()
        btn2.destroy()
        self.tabs.remove((btn, btn2))

    def on_tab_button(self,btn):
        btn.configure(fg_color=("blue"))

    def get_data_for_request(self):
        data =  self.tab_body.get_all_data()
        self.callback(data)


