import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import psutil
import wmi





class DiskInfoUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Disk")
        self.style = ThemedStyle(self.root)
        self.style.set_theme("equilux")
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Disk info label
        self.disk_info_label = ttk.Label(self.frame, font=('Arial', 12), anchor=tk.W, justify=tk.LEFT)
        self.disk_info_label.pack(fill=tk.BOTH, expand=True)

        # Update button
        self.update_button = ttk.Button(self.frame, text="Update", command=self.refresh_disk_info)
        self.update_button.pack(side=tk.LEFT, padx=5, pady=10)

        # Exit button
        self.exit_button = ttk.Button(self.frame, text="Exit", command=self.root.destroy)
        self.exit_button.pack(side=tk.LEFT, padx=5, pady=10)

        # Create an instance of DiskInfo class
        self.disk_info = DiskInfo()

        # Refresh disk info on startup
        self.refresh_disk_info()

        self.root.mainloop()

    def refresh_disk_info(self):
        disk_info = self.disk_info.refresh_disk_info()
        self.disk_info_label.config(text=disk_info)


if __name__ == '__main__':
    DiskInfoUI()
