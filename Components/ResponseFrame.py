import customtkinter as ctk 
import json
from bs4 import BeautifulSoup

class ResponseFrame(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.response= None
        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)

        self.label = ctk.CTkLabel(self,text="Response",font=("Arial", 16, "bold"))
        self.label.grid(row=0,column=0,padx=10,pady=10)

        self.label2 = ctk.CTkLabel(self,text="Status Code")
        self.label2.grid(row=0,column=2,padx=10)

        self.btn = ctk.CTkOptionMenu(self,height=30,values=["HTML","JSON","RAW"],command=self.pretify)
        self.btn.grid(row=0,column=3,padx=(10),pady=10)

        self.progress = ctk.CTkProgressBar(self,orientation="horizontal",width=10,mode="indeterminate",indeterminate_speed=2)
        self.progress.grid(row=1,column=0,columnspan=4,sticky="ew",padx=10)

        self.textbox = ctk.CTkTextbox(self,font=("Arial", 15, "normal"))
        self.textbox.configure(state="disabled")
        self.textbox.grid(row=2,column=0,columnspan=4,sticky="ewns",padx=10,pady=(0,10))
    
    def recieve_and_emit_reponse(self,response):
        self.progress.stop()
        if isinstance(response, BaseException):
            self.print_data(type(response).__name__)
            return
        if not response or not response.status_code:
            self.print_data("Something went wrong :(")
            return 
        if response.status_code:
            self.label2.configure(text=f"Status Code:{response.status_code} {self.get_status_message(response.status_code)}        Time:{int(response.elapsed.total_seconds() * 1000)}ms")
        self.response = response
        data_type = self.detect_data_type(response)
        self.btn.set(value=data_type)
        self.display(data_type,response)

    def display(self,data_type,response):
        if (data_type=="JSON"):
            response = json.dumps(response.json(), indent=4)
            self.print_data(response)
        elif data_type=="HTML":
            soup = BeautifulSoup(response.text, "lxml")
            self.print_data(soup.prettify())
        else:
            self.print_data(response.content)

    def print_data(self,data):
        self.textbox.configure(state="normal")    
        self.textbox.delete("1.0", "end")            
        self.textbox.insert("1.0",data) 
        self.textbox.configure(state="disabled")

    def detect_data_type(self,response):
        content = response.text.strip()
        try:
            json.loads(content)
            return "JSON"
        except json.JSONDecodeError:
            pass

        if content.startswith("<") and bool(BeautifulSoup(content, "html.parser").find()):
            return "HTML"
        return "RAW"

    def pretify(self):
        pass

    def get_status_message(self,status_code):
        http_status_names = {
            200: "OK",
            201: "Created",
            202: "Accepted",
            204: "No Content",
    
            301: "Moved Permanently",
            302: "Found",
    
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            405: "Method Not Allowed",
            409: "Conflict",
    
            500: "Internal Server Error",
            501: "Not Implemented",
            502: "Bad Gateway",
            503: "Service Unavailable",
            504: "Gateway Timeout"
        }
        return http_status_names.get(status_code)
    def start_progress(self):
        self.progress.start()
