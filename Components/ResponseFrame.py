import customtkinter as ctk 

class ResponseFrame(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)

        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(1,weight=1)

        self.label = ctk.CTkLabel(self,text="Response",font=("Arial", 16, "bold"))
        self.label.grid(row=0,column=0,padx=10,pady=10)

        self.btn = ctk.CTkOptionMenu(self,height=30,values=["HTML","JSON"])
        self.btn.grid(row=0,column=2,padx=(10),pady=10)

        self.textbox = ctk.CTkTextbox(self,font=("Arial", 15, "bold"))
        self.textbox.configure(state="disabled")
        self.textbox.grid(row=1,column=0,columnspan=3,sticky="ewns",padx=10,pady=(0,10))