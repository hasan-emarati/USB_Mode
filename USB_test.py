import tkinter as tk
from tkinter import ttk
from tkinter import font
from ttkthemes import ThemedStyle
from USB import Disk

class DiskUI:
    def __init__(self):
        # ...
        
        # Change the position and size of main frame
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.frame.configure(width=700, height=250)

        # Change the position and size of buttons frame
        self.button_frame.place(relx=0.8, rely=0.5, anchor=tk.CENTER)
        self.button_frame.configure(width=250, height=250)

        # Change the position and size of checkboxes frame
        self.disk_checkboxes_frame.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
        self.disk_checkboxes_frame.configure(width=400, height=250)

        # Change the position and size of refresh button
        self.refresh_button.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        self.refresh_button.configure(width=100, height=30)

        # Change the position and size of read button
        self.read_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
        self.read_button.configure(width=100, height=30)

        # Change the position and size of read/write button
        self.read_write_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.read_write_button.configure(width=100, height=30)

        # Change the position and size of format disk button
        self.format_button.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        self.format_button.configure(width=100, height=30)

        # Change the position and size of eject disk button
        self.eject_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        self.eject_button.configure(width=100, height=30)

        # Change the position and size of reset button
        self.reset_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        self.reset_button.configure(width=100, height=30)

        # Change the position and size of exit button
        self.exit_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)
        self.exit_button.configure(width=100, height=30)

        # Reset button
        self.reset_button = ttk.Button(self.button_frame, text="Reset", command=self.reset, style="Yellow.TButton")
        self.reset_button.pack(side=tk.BOTTOM, padx=5, pady=10)

        # Set style for buttons
        self.style.configure("Yellow.TButton", background="#00ADB5", foreground="#EEEEEE", font=("Helvetica", 14), borderwidth=0, focuscolor="#ffffff", hovercolor="#F1C40F", highlightthickness=0, relief="flat")

        # Set style for checkboxes
        self.style.configure("Yellow.TCheckbutton", background="#393E46", foreground="#EEEEEE", font=("Helvetica", 14), focuscolor="#ffffff", highlightthickness=0, relief="flat")

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
        if action == "Eject_Disk":
            self.Eject_Disk()
        elif action == "Format_Disk":
            self.Format_Disk()
        elif action == "Read_Only":
            self.Read_Only()
        elif action == "Read_Write":
            self.Read_Write()

    def reset(self):
        self.root.destroy()
        DiskUI()

if __name__ == '__main__':
    DiskUI()