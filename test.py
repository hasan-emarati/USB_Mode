import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from USB import Disk
from tkinter import *

class DiskUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Disk")
        self.style = ThemedStyle(self.root)
        self.style.set_theme("equilux")
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.root.minsize(1000,150)
        self.root.maxsize(800,500)
        
        self.disk_info_label = ttk.Label(self.frame, font=('Arial', 12), anchor=tk.W, justify=tk.LEFT)
        self.disk_info_label.pack(fill=tk.BOTH, expand=True)

        self.update_button = ttk.Button(self.frame, text="Update", command=self.refresh_disk_info)
        self.update_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.only_read_button = ttk.Button(self.frame, text="Only Read", command=self.refresh_disk_info)
        self.only_read_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.read_write_button = ttk.Button(self.frame, text="Read/Write", command=self.refresh_disk_info)
        self.read_write_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.format_button = ttk.Button(self.frame, text="Format", command=self.format_disk)
        self.format_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.eject_button = ttk.Button(self.frame, text="Eject Disk", command=self.eject_disk)
        self.eject_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.exit_button = ttk.Button(self.frame, text="Exit", command=self.root.destroy)
        self.exit_button.pack(side=tk.RIGHT, padx=5, pady=10)

        self.disk = Disk()
        self.refresh_disk_info()

        self.root.mainloop()

    def refresh_disk_info(self):
        disk_info = self.disk.refresh_disk_info()
        self.disk_info_label.config(text=disk_info)

    def eject_disk(self):
        self.disk.eject_disk()

    def format_disk(self):
        self.disk.format_disk()

if __name__ == '__main__':
    DiskUI()
