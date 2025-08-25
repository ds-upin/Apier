import customtkinter as ctk
#import time
from Components.HeaderFrame import HeaderFrame
from Components.HistoryFrame import HistoryFrame
from Components.BodyFrame import BodyFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #self.iconify()
        #time.sleep(2)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title("EndLITE")
        self.attributes("-fullscreen", True)
        self.state("normal")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.no_tabs = 0
        self.tabs = []
        self.focused_frame = None
        self.focused_button = None

        
        self.header_frame = HeaderFrame(self)
        self.history_frame = HistoryFrame(self)
        self.tab_frame = ctk.CTkScrollableFrame(self, height=30, orientation="horizontal")
        self.add_tab_button = ctk.CTkButton(self.tab_frame, text="+", width=50, command=self.__add_tab, fg_color=("orange", "green"))
        self.__add_tab()
        self.header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.history_frame.grid(row=1, column=0, rowspan=2, sticky="nsw", padx=5, pady=5)
        self.tab_frame.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        

        #self.__add_tab()
        #self.after(5000, self.deiconify)
        
    def toggle_fullscreen(self):
        self.attributes("-fullscreen", not self.attributes("-fullscreen"))
    
    def history_data(self,data):
        self.history_frame.add_history(data)

    def __add_tab(self):
        tab_index = self.no_tabs
        body_frame = BodyFrame(self)

        btn = ctk.CTkButton(
            self.tab_frame, width=70, text=f"Tab {tab_index}",
            command=lambda: self.focus_frame(body_frame, btn),
            fg_color="transparent"
        )
        btn2 = ctk.CTkButton(
            self.tab_frame, width=20, text="x",
            command=lambda: self.remove_tab(btn, btn2, body_frame),
            fg_color="transparent", hover_color="red"
        )

        if self.focused_frame and self.focused_frame.winfo_exists():
            self.focused_frame.grid_remove()

        body_frame.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
        self.focus_frame(body_frame, btn)

        btn.grid(row=0, column=tab_index * 2)
        btn2.grid(row=0, column=tab_index * 2 + 1, padx=(0, 5))

        self.tabs.append((btn, btn2, body_frame))
        self.no_tabs += 1

        self.add_tab_button.grid(row=0, column=self.no_tabs * 2, padx=(0, 5))

    def remove_tab(self, btn, btn2, body_frame):
        if len(self.tabs) == 1:
            return 
        self.tabs.remove((btn, btn2, body_frame))
        btn.destroy()
        btn2.destroy()
        body_frame.destroy()

        self.no_tabs -= 1
        for index, (b, b2, _) in enumerate(self.tabs):
            b.grid(row=0, column=index * 2)
            b.configure(text=f"Tab {index}")
            b2.grid(row=0, column=index * 2 + 1, padx=(0, 5))

        self.add_tab_button.grid(row=0, column=len(self.tabs) * 2, padx=(0, 5))
        if self.focused_frame == body_frame:
            last_btn, _, last_frame = self.tabs[-1]
            self.focus_frame(last_frame, last_btn)

    def focus_frame(self, body_frame, btn):
        if self.focused_frame and self.focused_frame.winfo_exists():
            self.focused_frame.grid_remove()

        body_frame.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
        self.focused_frame = body_frame
        self.focused_button = btn

if __name__ == "__main__":
    app = App()
    #app.withdraw()
    app.mainloop()
