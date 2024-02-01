import tkinter as tk
from tkinter import ttk

class Buttons:
    def __init__(self, root, functions):
        self.root = root
        self.functions = functions

        self.create_buttons()

    def create_buttons(self):
        self.browse_button = ttk.Button(self.root, text="Browse", command=self.functions.browse_output_location)
        self.browse_button.grid(row=2, column=2, padx=10, pady=10, sticky=tk.W)

        self.scrape_button = ttk.Button(self.root, text="Scrape", command=self.functions.scrape_website)
        self.scrape_button.grid(row=3, column=1, padx=10, pady=20, sticky=tk.W)
