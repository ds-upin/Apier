import customtkinter as ctk

class KeyValueTableFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.grid(row=0, column=0, sticky="nsew")

        self.scroll_frame.grid_columnconfigure(1, weight=1)
        self.scroll_frame.grid_columnconfigure(2, weight=3)

        self.rows = []
        self.add_row()

    def add_row(self):
        row_index = len(self.rows)

        var = ctk.BooleanVar()
        checkbox = ctk.CTkCheckBox(self.scroll_frame, variable=var,text="",width=20)
        key_entry = ctk.CTkEntry(self.scroll_frame, placeholder_text="Key")
        value_entry = ctk.CTkEntry(self.scroll_frame, placeholder_text="Value")

        checkbox.grid(row=row_index, column=0, padx=5, pady=5)
        key_entry.grid(row=row_index, column=1, sticky="ew", padx=5, pady=5)
        value_entry.grid(row=row_index, column=2, sticky="ew", padx=5, pady=5)

        key_entry.bind("<KeyRelease>", lambda e, entry=key_entry: self.on_key_input(entry))

        self.rows.append((checkbox, key_entry, value_entry))

    def on_key_input(self, entry):
        row_idx = next((i for i, (_, e, _) in enumerate(self.rows) if e == entry), None)
        if row_idx is not None and row_idx == len(self.rows) - 1:
            key_text = entry.get()
            if key_text.strip() != "":
                self.add_row()

    def get_data(self):
        result = {}
        for checkbox, key_entry, value_entry in self.rows:
            is_checked = checkbox.get()
            key = key_entry.get().strip()
            value = value_entry.get()

            if is_checked and key:
                result[key] = value.strip() if value else ""
        return result