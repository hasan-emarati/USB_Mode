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
        
        # Disk info label
        self.disk_info_label = ttk.Label(self.frame, font=('Arial', 12), anchor=tk.W, justify=tk.LEFT)
        self.disk_info_label.pack(fill=tk.BOTH, expand=True)

        # Update button
        self.update_button = ttk.Button(self.frame, text="Update", command=self.refresh_disk_info)
        self.update_button.pack(side=tk.LEFT, padx=5, pady=10 , )

        # Only Read button
        self.update_button = ttk.Button(self.frame, text="Only Read", command=self.Read_Only)
        self.update_button.pack(side=tk.LEFT, padx=5, pady=10)

        # Read/Write button
        self.update_button = ttk.Button(self.frame, text="Read/Write", command=self.Read_Write)
        self.update_button.pack(side=tk.LEFT, padx=5, pady=10)

        # Format Disk button
        self.update_button = ttk.Button(self.frame, text="Format", command=self.Format_Disk)
        self.update_button.pack(side=tk.LEFT, padx=5, pady=10)

        # Eject Disk button
        self.exit_button = ttk.Button(self.frame, text="Eject Disk", command=self.Eject_Disk)
        self.exit_button.pack(side=tk.LEFT, padx=5, pady=10)

        # Exit button
        self.exit_button = ttk.Button(self.frame, text="Exit", command=self.root.destroy)
        self.exit_button.pack(side=tk.RIGHT, padx=5, pady=10)

        # Create an instance of Disk class
        self.disk_info = Disk()
        self.Eject = Disk()
        self.Format = Disk() 
        self.Read = Disk()
        self.Write = Disk()


        # Refresh disk info on startup
        self.refresh_disk_info()
        # self.Eject_Disk()
        # self.Format_Disk()

        self.root.mainloop()

    def refresh_disk_info(self):
        disk_info = self.disk_info.refresh_disk_info()
        self.disk_info_label.config(text=disk_info)

    def Eject_Disk(self):
        Eject = self.Eject.Eject_Disk()
    
    def Format_Disk(self):
        Format = self.Format.Format_Disk()

    def Read_Only(self):
        Read = self.Read.Read_Only()

    def Read_Write(self):
        Write = self.Write.Read_Write()

if __name__ == '__main__':
    DiskUI()

