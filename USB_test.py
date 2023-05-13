import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import wmi

class Disk:
    def refresh_disk_info(self):
        c = wmi.WMI()
        disk_info = []
        for disk in c.Win32_LogicalDisk():
            free_space = round(int(disk.FreeSpace)/(1024**3), 2) if disk.FreeSpace is not None else "-"
            size = round(int(disk.Size)/(1024**3), 2) if disk.Size is not None else "-"
            disk_info += [f'{disk.DeviceID}{disk.VolumeName} Free Space: {free_space} GB Size: {size} GB File System: {disk.FileSystem} VolumeDirty: {disk.VolumeDirty} Serial Number: {disk.VolumeSerialNumber}']
        return disk_info
    
    def Eject_Disk(self):
        print("Disk is Ejecting")
        
    def Format_Disk(self):
        print("Formatting disk")
        
    def Read_Only(self):
        print("Read-Only")
        
    def Read_Write(self):
        print("Read/Write")
        
    def perform_action(self, action, selected_items):
        # Print selected items
        print("Selected items:", selected_items)

        # Perform action on selected items
        if action == "Eject_Disk":
            self.Eject_Disk()
        elif action == "Format_Disk":
            self.Format_Disk()
        elif action == "Read_Only":
            self.Read_Only()
        elif action == "Read_Write":
            self.Read_Write()

class DiskUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Disk")
        self.style = ThemedStyle(self.root)
        self.style.set_theme("equilux")
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.root.minsize(400, 200)
        self.root.maxsize(800, 500)

        # Create an instance of Disk class
        self.disk_info = Disk()

        # Disk info checkboxes
        self.disk_checkboxes_frame = ttk.Frame(self.frame)
        self.disk_checkboxes_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.disk_checkboxes = []
        self.refresh()

        # Button frame
        self.button_frame = ttk.Frame(self.frame)
        self.button_frame.pack(side=tk.LEFT)

        # Refresh button
        self.refresh_button = ttk.Button(self.button_frame, text="Refresh", command=self.refresh)
        self.refresh_button.pack(side=tk.TOP, padx=5, pady=10)

        # Only Read button
        self.read_button = ttk.Button(self.button_frame, text="Only Read", command=lambda: self.perform_action("Read_Only", self.get_selected_items()))
        self.read_button.pack(side=tk.TOP, padx=5, pady=10)

        # Read/Write button
        self.read_write_button = ttk.Button(self.button_frame, text="Read/Write", command=lambda: self.perform_action("Read_Write", self.get_selected_items()))
        self.read_write_button.pack(side=tk.TOP, padx=5, pady=10)

        # Eject button
        self.eject_button = ttk.Button(self.button_frame, text="Eject", command=lambda: self.perform_action("Eject_Disk", self.get_selected_items()))
        self.eject_button.pack(side=tk.TOP, padx=5, pady=10)

        # Format button
        self.format_button = ttk.Button(self.button_frame, text="Format", command=lambda: self.perform_action("Format_Disk", self.get_selected_items()))
        self.format_button.pack(side=tk.TOP, padx=5, pady=10)

        self.root.mainloop()

    def refresh(self):
        # Clear checkboxes
        for checkbox in self.disk_checkboxes:
            checkbox.destroy()
        self.disk_checkboxes = []

        # Get disk info and create checkboxes
        disk_info = self.disk_info.refresh_disk_info()
        for item in disk_info:
            checkbox = ttk.Checkbutton(self.disk_checkboxes_frame, text=item)
            checkbox.pack(side=tk.TOP, anchor=tk.W)
            self.disk_checkboxes.append(checkbox)

    def get_selected_items(self):
        selected_items = []
        for checkbox in self.disk_checkboxes:
            if checkbox.instate(['selected']):
                selected_items.append(checkbox['text'])
        return selected_items

    def perform_action(self, action, selected_items):
        self.disk_info.perform_action(action, selected_items)

DiskUI()