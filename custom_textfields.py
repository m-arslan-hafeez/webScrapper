import tkinter as tk
from tkinter import ttk, filedialog

class TextFields:
    def __init__(self, root, app):
        self.root = root
        self.app = app

        self.create_text_fields()

    def create_text_fields(self):
        self.label_url = ttk.Label(self.root, text="Enter Website URL:")
        self.label_url.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.url_entry = ttk.Entry(self.root, width=40)
        self.url_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.label_output = ttk.Label(self.root, text="Select Output CSV Location:")
        self.label_output.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.output_entry = ttk.Entry(self.root, width=40)
        self.output_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
