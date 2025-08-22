import customtkinter as ctk

ctk.set_appearance_mode("System")  # Options: "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # Optional: blue, green, dark-blue, etc.

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CTkTabview Example")
        self.geometry("500x400")

        # Create Tabview
        tabview = ctk.CTkTabview(self, width=480, height=350)
        tabview.pack(padx=20, pady=20, fill="both", expand=True)

        # Add tabs
        tabview.add("Tab 1")
        tabview.add("Tab 2")
        tabview.add("Tab 3")

        # Access tabs via tabview.tab("Tab Name")
        tab1 = tabview.tab("Tab 1")
        tab2 = tabview.tab("Tab 2")
        tab3 = tabview.tab("Tab 3")

        # Add widgets to Tab 1
        ctk.CTkLabel(tab1, text="This is Tab 1").pack(pady=10)
        ctk.CTkEntry(tab1, placeholder_text="Enter something").pack(pady=5)

        # Add widgets to Tab 2
        ctk.CTkLabel(tab2, text="This is Tab 2").pack(pady=10)
        ctk.CTkButton(tab2, text="Click Me").pack(pady=5)

        # Tab 3 can be empty or filled later

if __name__ == "__main__":
    app = App()
    app.mainloop()
