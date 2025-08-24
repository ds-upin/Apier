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
        self.focused_frame = None
        self.focused_button= None
        self.grid_columnconfigure((1),weight=1)
        self.grid_rowconfigure(2,weight=1)
        self.header_frame = HeaderFrame(self)
        self.header_frame.grid(row=0,column=0,columnspan=2, sticky="ew")

        self.history_frame = HistoryFrame(self)
        self.history_frame.grid(row=1,column=0,rowspan=2,sticky="wsn",pady=(5,5),padx=(5,5))
        
        self.no_tabs = 1
        self.tabs = []
        self.tab_frame = ctk.CTkScrollableFrame(self,height=30,orientation="horizontal")
        self.tab_frame.grid(row=1,column=1,padx=(5,5),pady=(5,5),sticky="ew")

        for i in range(self.no_tabs):
            self.add_tab()
        self.tab = ctk.CTkButton(self.tab_frame,text="+",width=50,command=self.add_tab, fg_color=("orange","green"))
        self.tab.grid(row=0,column=1000)

        #self.body_frame = BodyFrame(self)
        #self.body_frame.grid(row=,column=1,sticky="nsew",pady=(5,5),padx=(5,5))
        self.state("normal")

    def zooms(self):
        self.iconify()

    def add_tab(self):
        tab_index = self.no_tabs
        body_frame = BodyFrame(self)
        btn = ctk.CTkButton(self.tab_frame, width=70, text=f"Tab {tab_index}",command=lambda: self.focus_frame(body_frame), fg_color="transparent")
        btn2 = ctk.CTkButton(self.tab_frame, width=20, text="x",command=lambda: self.remove_tab(btn,btn2,body_frame) ,fg_color="transparent", hover_color=("red","red"))
        
        #forgot all frames
        if self.focused_frame is not None:
            self.focused_frame.grid_remove()

        body_frame.grid(row=2,column=1,sticky="nsew",pady=(5,5),padx=(5,5))
        self.focused_frame = body_frame
        btn.grid(row=0, column=tab_index*2)
        btn2.grid(row=0, column=tab_index*2+1,padx=(0,5))
    
        self.no_tabs += 1
        self.tabs.append((btn, btn2,body_frame))

    def remove_tab(self, btn, btn2,body_frame):
        if (len(self.tabs)==1):
            return 
        btn.destroy()
        btn2.destroy()
        body_frame.destroy()
        self.tabs.remove((btn, btn2,body_frame))
        if self.tabs:
            self.focus_frame(self.tabs[-1][2])
            self.focused_frame=self.tabs[-1][2]
    def focus_frame(self,body_frame):
        self.focused_frame.grid_remove()
        body_frame.grid(row=2,column=1,sticky="nsew",pady=(5,5),padx=(5,5))
        self.focused_frame=body_frame
        
        


app = App()
app.mainloop()

        