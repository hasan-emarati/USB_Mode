import tkinter as tk
from tkinter import ttk
from tkinter import font
from ttkthemes import ThemedStyle
from USB import Disk

class DiskUI:
    def __init__(self):
        self.disk = Disk()
        self.root = tk.Tk()
        self.root.title("DiskUI")
        self.style = ThemedStyle(self.root)
        self.style.theme_use("equilux")  
        self.style.configure("TFrame", background="#363636")
        self.frame = ttk.Frame(self.root, padding=15)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.root.minsize(800, 300)
        self.root.maxsize(1400, 500)

        # Change font size of text
        default_font = font.nametofont("TkDefaultFont").configure(size=14)

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
        self.refresh_button = ttk.Button(self.button_frame, text="Refresh", command=self.refresh, style="Yellow.TButton")
        self.refresh_button.pack(side=tk.TOP, padx=5, pady=10 ,)

        # Only Read button
        self.read_button = ttk.Button(self.button_frame, text="Only Read", command=lambda: self.perform_action("Read_Only"), style="Yellow.TButton")
        self.read_button.pack(side=tk.TOP, padx=5, pady=10)

        # Read/Write button
        self.read_write_button = ttk.Button(self.button_frame, text="Read/Write", command=lambda: self.perform_action("Read_Write"), style="Yellow.TButton")
        self.read_write_button.pack(side=tk.TOP, padx=5, pady=10)

        # Format Disk button
        self.format_button = ttk.Button(self.button_frame, text="Format", command=lambda: self.perform_action("Format_Disk"), style="Yellow.TButton")
        self.format_button.pack(side=tk.TOP, padx=5, pady=10)

        # Eject Disk button
        self.eject_button = ttk.Button(self.button_frame, text="Eject Disk", command=lambda: self.perform_action("Eject_Disk"), style="Yellow.TButton")
        self.eject_button.pack(side=tk.TOP, padx=5, pady=10)

        # Exit button
        self.exit_button = ttk.Button(self.button_frame, text="Exit", command=self.root.destroy, style="Yellow.TButton")
        self.exit_button.pack(side=tk.BOTTOM, padx=5, pady=10)

        # Reset button
        self.reset_button = ttk.Button(self.button_frame, text="Reset", command=self.reset, style="Yellow.TButton")
        self.reset_button.pack(side=tk.BOTTOM, padx=5, pady=10)

        # Set style for buttons
        self.style.configure("Yellow.TButton", background="#7F5283", foreground="#00ADB5", font=("Helvetica", 14), borderwidth=0, focuscolor="#ffffff", hovercolor="#F1C40F", highlightthickness=0, relief="flat")

        # Set style for checkboxes
        self.style.configure("Yellow.TCheckbutton", background="#252525", foreground="#E46D6D", font=("Helvetica", 14), focuscolor="#00ADB5", highlightthickness=0, relief="flat")

        self.root.mainloop()

    def refresh(self):
        # Refresh disk info checkboxes
        for checkbox in self.disk_checkboxes:
            checkbox.destroy()
        self.disk_checkboxes.clear()
        disk_info = self.disk_info.refresh_disk_info()
        for disk in disk_info:
            checkbox = ttk.Checkbutton(self.disk_checkboxes_frame, text=disk, variable=tk.BooleanVar(), style="Yellow.TCheckbutton")
            checkbox.pack(anchor=tk.W, fill=tk.BOTH, expand=True)
            self.disk_checkboxes.append(checkbox)

    def Eject_Disk(self):
        self.disk_info.Eject_Disk()

    def Format_Disk(self):
        self.disk_info.Format_Disk()

    def Read_Only(self):
        self.disk_info.Read_Only()

    def Read_Write(self):
        self.disk_info.Read_Write()

    def perform_action(self, action):
        # Print selected items
        selected_items = [checkbox.cget("text") for checkbox in self.disk_checkboxes if checkbox.instate(['selected'])]
        print("Selected items:", selected_items)

        # Perform action on selected items
        if len(selected_items) > 0:
            if action == "Eject_Disk":
                self.disk.Eject_Disk(selected_items)
            elif action == "Format_Disk":
                self.disk.Format_Disk(selected_items)
            elif action == "Read_Only":
                self.disk.Read_Only(selected_items)
            elif action == "Read_Write":
                self.disk.Read_Write(selected_items)
                
        return selected_items

    def reset(self):
        self.root.destroy()
        DiskUI()

if __name__ == '__main__':
    DiskUI()