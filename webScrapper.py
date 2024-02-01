from datetime import datetime
import getpass
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from custom_buttons import Buttons
from custom_textfields import TextFields
from functions import Functions
from menu_functions import *

class WebScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Scraping Application")

        # Set window size and disable resizing
        self.root.geometry("500x250")
        self.root.resizable(width=False, height=False)

        # Disable maximize button
        self.root.attributes('-toolwindow', 1)

        style = ThemedStyle(root)
        style.set_theme("radiance")  # Choose a theme ("radiance", "aquativo", "arc", etc.)

        self.textfields = TextFields(self.root, self)  # Create TextFields instance
        self.functions = Functions(self)  # Pass TextFields instance to Functions

        self.buttons = Buttons(self.root, self.functions)

        self.create_menu()  # Create menu bar

        self.create_status_bar()

        # Allow rows and columns to grow and shrink with window resizing
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(1, weight=1)

        # Add a resizing grip at the bottom-right corner
        ttk.Sizegrip(root).grid(row=999, column=999, sticky=(tk.W, tk.S))

        # Initialize status bar visibility
        self.status_bar_visible = tk.BooleanVar(value=True)

    def create_menu(self):
        menubar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label="Status", command=self.toggle_status_bar)
        menubar.add_cascade(label="View", menu=view_menu)

        # Settings menu
        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label="General Settings", command=general_settings)
        menubar.add_cascade(label="Settings", menu=settings_menu)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=about)
        help_menu.add_command(label="Contact", command=contact)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)


    def create_status_bar(self):
        self.status_bar = ttk.Label(self.root, text="", anchor=tk.W)
        self.status_bar.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E))

    def toggle_status_bar(self):
        self.status_bar_visible.set(not self.status_bar_visible.get())
        if self.status_bar_visible.get():
            self.status_bar.grid()
        else:
            self.status_bar.grid_remove()

    def update_status_bar(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        username = getpass.getuser()
        status_text = f"Date/Time: {current_time}  |  User: {username}"
        self.status_bar.config(text=status_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = WebScraperApp(root)
    app.update_status_bar()  # Initialize status bar content
    root.after(1000, app.update_status_bar)  # Update status bar every second
    root.mainloop()
