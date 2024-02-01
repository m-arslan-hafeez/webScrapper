import requests
from bs4 import BeautifulSoup
import csv
from tkinter import filedialog, messagebox
import tkinter as tk

class Functions:
    def __init__(self, app):
        self.app = app
        self.textfields = app.textfields

    def scrape_website(self):
        url = self.textfields.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a valid URL.")
            return

        output_file_path = self.textfields.output_entry.get()
        if not output_file_path:
            messagebox.showerror("Error", "Please select an output CSV location.")
            return

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch the website: {e}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        scraped_data = self.process_data(soup)

        self.save_to_csv(scraped_data, output_file_path)

        messagebox.showinfo("Scraping Complete", "Scraping has been completed successfully.")

    def process_data(self, soup):
        # Extract text from all HTML tags
        all_text = [tag.get_text() for tag in soup.find_all(True)]
        return all_text

    def save_to_csv(self, data, file_path):
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Scraped Data'])
            for item in data:
                csv_writer.writerow([item])

    def browse_output_location(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        self.textfields.output_entry.delete(0, tk.END)
        self.textfields.output_entry.insert(0, file_path)
