import customtkinter as ctk

class HeaderFrame(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.master=master

        self.grid_columnconfigure((0,),weight=1)

        self.head_label = ctk.CTkLabel(self,text="APIER",font=("Helvetica",20,"bold"))
        self.head_label.grid(row=0,column=0,padx=10,pady=(10,10))
        
        self.btn1 = ctk.CTkButton(self,text="_",height=30,width=30, command=self.minimize_window)
        self.btn1.grid(row=0,column=1,padx=(5,5),pady=(10,10))

        self.btn2 = ctk.CTkButton(self,text="🗖",height=30,width=30,command=self.toggle_maximize)
        self.btn2.grid(row=0,column=2,padx=(5,5),pady=(10,10))

        self.btn3 = ctk.CTkButton(self,text="X",hover_color=("red","red"),height=30,width=30,command=master.destroy)
        self.btn3.grid(row=0,column=3,padx=(5,5),pady=(10,10))

    def toggle_maximize(self):
        #self.master.withdraw()
        self.master.state('zoomed')

        #self.master.update_idletasks()
        #self.master.after(50,lambda: self.master.deiconify())
        

    def minimize_window(self):
        self.master.iconify()

