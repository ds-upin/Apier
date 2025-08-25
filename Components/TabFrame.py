import customtkinter as ctk 
from .ParamsFrame import AttributeEntryFrame

class TabFrame(ctk.CTkFrame):
    def __init__(self,master,callback=None,start_progress_callback1=None,**kwargs):
        super().__init__(master,**kwargs)
        self.callback=callback
        self.start_progress_callback1=start_progress_callback1
        
        self.data = {"http_method":dict(),"url":"","params":dict(),"headers":dict(),"body":dict(),"cookies":dict(),"test":list(),"prerequset":list()}

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure((2),weight=1)

        self.attribute_frame_autherization = AttributeEntryFrame(self,labeled="autherization",fg_color="transparent")
        self.attribute_frame_params = AttributeEntryFrame(self,labeled="params",fg_color="transparent")
        self.attribute_frame_headers = AttributeEntryFrame(self,labeled="headers",fg_color="transparent")
        self.attribute_frame_body = AttributeEntryFrame(self,labeled="body",fg_color="transparent")
        self.attribute_frame_test = AttributeEntryFrame(self,labeled="test",fg_color="transparent")
        self.attribute_frame_cookies = AttributeEntryFrame(self,labeled="cookies",fg_color="transparent")
        self.attribute_frame_prerequest = AttributeEntryFrame(self,labeled="pre-request",fg_color="transparent")



        self.request_option_frame = ctk.CTkFrame(self,fg_color="transparent")
        self.option_menu = ctk.CTkOptionMenu(self.request_option_frame,height=35,values=["GET","POST","PATCH","PUT","HEAD","OPTIONS","DELETE"])
        self.url_entry = ctk.CTkEntry(self.request_option_frame,height=35,placeholder_text="Enter URL...")
        self.send_btn = ctk.CTkButton(self.request_option_frame,text="SEND",height=35,width=100,command=self.get_all_data)
        self.request_attribute_option_frame = ctk.CTkFrame(self)
        self.param_btn = ctk.CTkButton(self.request_attribute_option_frame,command=lambda :self.select_attribute(self.attribute_frame_params),width=30,text="Params",fg_color="transparent")
        self.auth_btn = ctk.CTkButton(self.request_attribute_option_frame,width=30,text="Autherization",command=lambda :self.select_attribute(self.attribute_frame_autherization),fg_color="transparent")
        self.header_btn = ctk.CTkButton(self.request_attribute_option_frame,width=30,text="Headers",fg_color="transparent",command=lambda :self.select_attribute(self.attribute_frame_headers))
        self.body_btn = ctk.CTkButton(self.request_attribute_option_frame,width=30,text="Body",fg_color="transparent",command=lambda :self.select_attribute(self.attribute_frame_body))
        self.prerequest_btn = ctk.CTkButton(self.request_attribute_option_frame,width=30,text="Pre-request",fg_color="transparent",command=lambda :self.select_attribute(self.attribute_frame_prerequest))
        self.test_btn = ctk.CTkButton(self.request_attribute_option_frame,text="Test",width=30,fg_color="transparent",command=lambda :self.select_attribute(self.attribute_frame_test))
        self.cookies_btn = ctk.CTkButton(self.request_attribute_option_frame,text="Cookies",width=30,fg_color="transparent",command=lambda :self.select_attribute(self.attribute_frame_cookies))

        self.select_attribute(self.attribute_frame_params)
        self.request_attribute_option_frame.grid_columnconfigure(7,weight=1)
        self.selected_attribute = "params"
        self.request_option_frame.grid(row=0,column=0,padx=(20,10),pady=(30,30),sticky="ew")
        self.request_option_frame.grid_columnconfigure(1,weight=1)
        self.option_menu.set(value="GET")
        self.option_menu.grid(row=0,column=0)
        self.url_entry.grid(row=0,column=1,sticky="ew")
        self.send_btn.grid(row=0,column=2)
        self.request_attribute_option_frame.grid(row=1,column=0,sticky="ew",padx=20)
        self.param_btn.grid(row=0,column=0)
        self.auth_btn.grid(row=0,column=1)
        self.header_btn.grid(row=0,column=2)
        self.body_btn.grid(row=0,column=3)
        self.prerequest_btn.grid(row=0,column=4)
        self.test_btn.grid(row=0,column=5)
        self.cookies_btn.grid(row=0,column=6)
        
        
        #self.implement_logic()
    def enable_button(self):
        self.send_btn.configure(state="normal")

    def select_attribute(self,attr):
        for frame in [
            self.attribute_frame_params,
            self.attribute_frame_autherization,
            self.attribute_frame_headers,
            self.attribute_frame_body,
            self.attribute_frame_test,
            self.attribute_frame_cookies,
            self.attribute_frame_prerequest,
        ]:
            frame.grid_forget()

        # Show the selected frame
        self.selected_attribute = attr
        attr.grid(row=2, column=0, padx=(20, 10), pady=(10, 20), sticky="nsew")

    def get_all_data(self):
        self.data["http_method"] = {"method": self.option_menu.get()}
        self.data["url"] = self.url_entry.get().strip()
        self.data["params"] = self.attribute_frame_params.get_data()
        self.data["headers"] = self.attribute_frame_headers.get_data()
        self.data["body"] = self.attribute_frame_body.get_data()
        self.data["cookies"] = self.attribute_frame_cookies.get_data()
        self.data["test"] = self.attribute_frame_test.get_data()
        self.data["prerequset"] = self.attribute_frame_prerequest.get_data()
        self.data["autherization"] = self.attribute_frame_autherization.get_data()
        #print(self.data)
        self.callback(self.data)
        self.start_progress_callback1()
        self.send_btn.configure(state="disabled")
        return self.data


        

