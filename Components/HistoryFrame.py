import customtkinter as ctk 

class HistoryFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=2)
        self.grid_rowconfigure(2,weight=1)

        self.labelh = ctk.CTkLabel(self,text="History",font=("Helvetica",15))
        self.labelh.grid(row=0,column=0,padx=(5,5),pady=(5,3),sticky="nw")

        self.scroll = ctk.CTkScrollableFrame(self,width=250)
        self.scroll.grid(row=1,column=0,padx=(5,10),pady=(5,5),sticky="ns")

        for i in range(30):
            label = ctk.CTkLabel(self.scroll, text=f"Label {i+1}")
            label.grid(row=i,column=0,pady=5, padx=10, sticky="w")

        self.coll_frame = ctk.CTkFrame(self,height=100,width=250)
        self.coll_frame.grid(row=2,column=0, padx=(5,10),pady=(5,5), sticky="nsew")