import customtkinter as ctk 
from .KeyValueTableFrame import KeyValueTableFrame

class AttributeEntryFrame(ctk.CTkFrame):
    def __init__(self,master,labeled,**kwargs):
        super().__init__(master,**kwargs)

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)

        self.labeled=labeled

        self.label = ctk.CTkLabel(self,text=self.labeled,fg_color="transparent")
        self.label.grid(row=0,column=0,sticky="w")

        self.table = KeyValueTableFrame(self)
        self.table.grid(row=1,column=0,sticky="nsew")
    def get_data(self):
        return self.table.get_data()