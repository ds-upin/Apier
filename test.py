import customtkinter as ctk
import threading
import time

class CoolProgressBar(ctk.CTkFrame):
    def __init__(self, master, width=400, height=30, text="Downloading..."):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        self.label = ctk.CTkLabel(self, text=text, font=("Segoe UI", 14))
        self.label.grid(row=0, column=0, padx=5, pady=(5, 0), sticky="w")

        self.progressbar = ctk.CTkProgressBar(self, width=width, height=height, corner_radius=10)
        self.progressbar.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

        self.progressbar.set(0)  # Start at 0

    def set_progress(self,master, value: float):
        """Set progress between 0.0 and 1.0"""
        self.progressbar.set(value)
        self.label.configure(text=f"Sending Data to your lover: {int(value * 100)}%")
        if value >= 1.0:
            self.after(500, master.destroy)

    def animate_progress(self, duration=5):
        """Simulate progress animation for demonstration"""
        def run():
            for i in range(101):
                self.set_progress(self,i / 100)
                time.sleep(duration / 100)
        threading.Thread(target=run, daemon=True).start()
        

# Demo usage
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Cool Progress Bar")
    app.geometry("500x150")
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)

    progress = CoolProgressBar(app)
    progress.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    # Start demo animation
    progress.animate_progress(duration=4)

    app.mainloop()
