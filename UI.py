import customtkinter as ctk
from USB import Disk


class DiskUI:
    def __init__(self):
        self.disk = Disk()  
        self.root = ctk.CTk() 
        self.root.title("DiskUI")
        self.root.geometry("800x330")  
        self.setup_ui()  
        self.root.mainloop()

    def setup_ui(self):
        ctk.set_appearance_mode("dark")

        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)

        self.disk_radiobuttons_frame = ctk.CTkScrollableFrame(self.frame)
        self.disk_radiobuttons_frame.pack(fill=ctk.BOTH, expand=True, pady=10)
        self.disk_radiobuttons = []
        self.selected_disk = ctk.StringVar()  # متغیر برای رادیو باکس‌ها
        self.refresh()

        self.button_frame = ctk.CTkFrame(self.frame)
        self.button_frame.pack(fill=ctk.X, pady=10)

        buttons = [
            ("Refresh", self.refresh),
            ("Only Read", lambda: self.perform_action("Read_Only")),
            ("Read/Write", lambda: self.perform_action("Read_Write")),
            ("Format", self.open_format_window),
            ("Eject Disk", lambda: self.perform_action("Eject_Disk")),
            ("Reset", self.reset),
            ("Exit", self.root.destroy),
        ]
        for text, command in buttons:
            self.create_button(text, command)

    def create_button(self, text, command):
        button = ctk.CTkButton(
            self.button_frame,
            text=text,
            command=command,
            width=100 if text != "Exit" else 80,  
            corner_radius=10, 
        )
        button.pack(side=ctk.LEFT, padx=5, pady=5, expand=True)

    def refresh(self):
        for radiobutton in self.disk_radiobuttons:
            radiobutton.destroy()
        self.disk_radiobuttons.clear()
        disk_info = self.disk.refresh_disk_info()  
        for disk in disk_info:
            radiobutton = ctk.CTkRadioButton(
                self.disk_radiobuttons_frame,
                text=disk,
                variable=self.selected_disk,
                value=disk, 
                corner_radius=10, 
            )
            radiobutton.pack(anchor=ctk.W, fill=ctk.BOTH, pady=5)
            self.disk_radiobuttons.append(radiobutton)

    def perform_action(self, action):
        selected_item = self.selected_disk.get()  
        print("Selected item:", selected_item)

        if selected_item:
            actions = {
                "Eject_Disk": self.disk.Eject_Disk,  
                "Format_Disk": self.disk.Format_Disk,
                "Read_Only": self.disk.Read_Only,  
                "Read_Write": self.disk.Read_Write,  
            }
            if action in actions:
                actions[action]([selected_item])  

    def open_format_window(self):
        format_window = ctk.CTkToplevel(self.root)
        format_window.title("Format Options")
        format_window.geometry("250x380")  
        format_window.resizable(False, False)

        format_frame = ctk.CTkFrame(format_window)
        format_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)

        usb_label = ctk.CTkLabel(format_frame, text="Select USB Drive:")
        usb_label.pack(anchor=ctk.W, pady=5)  
        self.usb_var = ctk.StringVar()
        usb_options = [disk.cget("text").split(" - ")[0] for disk in self.disk_radiobuttons] 
        usb_menu = ctk.CTkComboBox(format_frame, variable=self.usb_var, values=usb_options)
        usb_menu.pack(anchor=ctk.W, pady=5, fill=ctk.X)  

        volume_label = ctk.CTkLabel(format_frame, text="Volume Label:")
        volume_label.pack(anchor=ctk.W, pady=5)  
        self.volume_entry = ctk.CTkEntry(format_frame)
        self.volume_entry.pack(anchor=ctk.W, pady=5, fill=ctk.X)

        file_system_label = ctk.CTkLabel(format_frame, text="File System:")
        file_system_label.pack(anchor=ctk.W, pady=5)  
        self.file_system_var = ctk.StringVar(value="FAT32")
        file_system_options = ["FAT32", "NTFS", "exFAT"]
        file_system_menu = ctk.CTkComboBox(format_frame, variable=self.file_system_var, values=file_system_options)
        file_system_menu.pack(anchor=ctk.W, pady=5, fill=ctk.X)  

        self.quick_format_var = ctk.BooleanVar(value=True)
        quick_format_check = ctk.CTkCheckBox(
            format_frame,
            text="Quick Format",
            variable=self.quick_format_var,
        )
        quick_format_check.pack(anchor=ctk.W, pady=5) 

        button_frame = ctk.CTkFrame(format_frame)
        button_frame.pack(fill=ctk.X, pady=10)

        start_button = ctk.CTkButton(
            button_frame,
            text="Format",
            command=self.start_format,
            width=100,
            corner_radius=10,
        )
        start_button.pack(side=ctk.LEFT, padx=5, expand=True)

        close_button = ctk.CTkButton(
            button_frame,
            text="Close",
            command=format_window.destroy,
            width=100,
            corner_radius=10,
        )
        close_button.pack(side=ctk.LEFT, padx=5, expand=True)

        self.status_var = ctk.StringVar(value="Ready")  
        status_bar = ctk.CTkLabel(format_frame, textvariable=self.status_var)
        status_bar.pack(side=ctk.BOTTOM, fill=ctk.X, pady=5)

    def start_format(self):
        selected_usb = self.usb_var.get() 
        volume_label = self.volume_entry.get()
        file_system = self.file_system_var.get()
        quick_format = self.quick_format_var.get()

        self.status_var.set("Formatting... Please wait.")
        try:
            self.disk.Format_Disk(selected_usb, file_system, volume_label)
            self.root.after(3000, lambda: self.status_var.set("Format completed successfully!"))
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")

    def reset(self):
        self.root.destroy()
        DiskUI()


if __name__ == '__main__':
    DiskUI()