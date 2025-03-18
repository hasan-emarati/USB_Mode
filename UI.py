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
        self.configure_styles()  
        self.setup_ui()  
        self.root.mainloop()

    def configure_styles(self):
        self.style.configure("TFrame", background="#363636") # App background
        self.style.configure(    # Buttons Tab 
            "Rounded.TButton",
            background="#7F5283",
            foreground="#00ADB5",
            font=("Helvetica", 12),
            borderwidth=0,
            padding=5,
            bordercolor="#7F5283",
            lightcolor="#7F5283",
            darkcolor="#7F5283",
            borderradius=20,
        )
        self.style.map(
            "Rounded.TButton",
            background=[("active", "#0C75EE")],  # Hover background
            foreground=[("active", "#00F7FF")],  # Hover Text Color
        )
        self.style.configure(
            "Yellow.TCheckbutton",
            background="#252525",
            foreground="#E46D6D",
            font=("Helvetica", 12),
            focuscolor="#00ADB5",
            highlightthickness=0,
            relief="flat",
        )
        self.style.configure(
            "Status.TLabel",
            background="#252525",
            foreground="#00ADB5",
            font=("Helvetica", 10),
            padding=5,
        )

    def setup_ui(self):
        self.root.minsize(800, 300)
        self.root.maxsize(1400, 500)

        # Font Size
        font.nametofont("TkDefaultFont").configure(size=12)
        self.frame = ttk.Frame(self.root, padding=15)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # CheckBox Frame
        self.disk_checkboxes_frame = ttk.Frame(self.frame)
        self.disk_checkboxes_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.disk_checkboxes = []
        self.refresh()

        # Key Frame
        self.button_frame = ttk.Frame(self.frame)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
        # creating buttons
        buttons = [
            ("Refresh", self.refresh),
            ("Only Read", lambda: self.perform_action("Read_Only")),
            ("Read/Write", lambda: self.perform_action("Read_Write")),
            ("Format", self.open_format_window),  # تغییر به تابع جدید
            ("Eject Disk", lambda: self.perform_action("Eject_Disk")),
            ("Reset", self.reset),
            ("Exit", self.root.destroy),
        ]
        for text, command in buttons:
            self.create_button(text, command)

    def create_button(self, text, command):
        button = ttk.Button(
            self.button_frame,
            text=text,
            command=command,
            style="Rounded.TButton",
            width=10 if text != "Exit" else 5,  # تنظیم عرض دکمه Exit
        )
        button.pack(side=tk.LEFT, padx=5, pady=5, expand=True)

    def refresh(self):
        for checkbox in self.disk_checkboxes:
            checkbox.destroy()
        self.disk_checkboxes.clear()
        disk_info = self.disk.refresh_disk_info()  
        for disk in disk_info:
            checkbox = ttk.Checkbutton(
                self.disk_checkboxes_frame,
                text=disk,
                variable=tk.BooleanVar(),
                style="Yellow.TCheckbutton",
            )
            checkbox.pack(anchor=tk.W, fill=tk.BOTH, expand=True)
            self.disk_checkboxes.append(checkbox)

    def perform_action(self, action):
        selected_items = [
            checkbox.cget("text")
            for checkbox in self.disk_checkboxes
            if checkbox.instate(['selected'])
        ]
        print("Selected items:", selected_items)

        if selected_items:
            actions = {
                "Eject_Disk": self.disk.Eject_Disk,  
                "Format_Disk": self.disk.Format_Disk,
                "Read_Only": self.disk.Read_Only,  
                "Read_Write": self.disk.Read_Write,  
            }
            if action in actions:
                actions[action](selected_items)

    def open_format_window(self):
        """باز کردن پنجره جدید برای فرمت."""
        format_window = tk.Toplevel(self.root)
        format_window.title("Format Options")
        format_window.geometry("400x450")  # تغییر اندازه پنجره به 400x450
        format_window.resizable(False, False)

        # تنظیم تم پنجره فرمت
        format_window.configure(bg="#363636")
        format_frame = ttk.Frame(format_window, padding=15)
        format_frame.pack(fill=tk.BOTH, expand=True)

        # Select USB Drive
        usb_label = ttk.Label(format_frame, text="Select USB Drive:", background="#363636", foreground="#00ADB5")
        usb_label.pack(anchor=tk.W, pady=5, fill=tk.X)  # پر کردن عرض
        self.usb_var = tk.StringVar()
        usb_options = [disk.cget("text").split(" - ")[0] for disk in self.disk_checkboxes]  # فقط درایو و نام دیسک
        usb_menu = ttk.Combobox(format_frame, textvariable=self.usb_var, values=usb_options, state="readonly", width=30)  # افزایش عرض Combobox
        usb_menu.pack(anchor=tk.W, pady=5, fill=tk.X)  # پر کردن عرض

        # Volume Label
        volume_label = ttk.Label(format_frame, text="Volume Label:", background="#363636", foreground="#00ADB5")
        volume_label.pack(anchor=tk.W, pady=5, fill=tk.X)  # پر کردن عرض
        self.volume_entry = ttk.Entry(format_frame, width=30)
        self.volume_entry.pack(anchor=tk.W, pady=5, fill=tk.X)  # پر کردن عرض

        # File System
        file_system_label = ttk.Label(format_frame, text="File System:", background="#363636", foreground="#00ADB5")
        file_system_label.pack(anchor=tk.W, pady=5, fill=tk.X)  # پر کردن عرض
        self.file_system_var = tk.StringVar(value="FAT32")
        file_system_options = ["FAT32", "NTFS", "exFAT"]
        file_system_menu = ttk.Combobox(format_frame, textvariable=self.file_system_var, values=file_system_options, state="readonly")
        file_system_menu.pack(anchor=tk.W, pady=5, fill=tk.X)  # پر کردن عرض

        # Quick Format
        self.quick_format_var = tk.BooleanVar(value=True)
        quick_format_check = ttk.Checkbutton(
            format_frame,
            text="Quick Format",
            variable=self.quick_format_var,
            style="Yellow.TCheckbutton",
        )
        quick_format_check.pack(anchor=tk.W, pady=5, fill=tk.X)  # پر کردن عرض

        # دکمه‌های Format و Close کنار هم
        button_frame = ttk.Frame(format_frame)
        button_frame.pack(fill=tk.X, pady=10)

        # Start Button
        start_button = ttk.Button(
            button_frame,
            text="Format",
            command=self.start_format,
            style="Rounded.TButton",
            width=10,
        )
        start_button.pack(side=tk.LEFT, padx=5, expand=True)

        # Close Button
        close_button = ttk.Button(
            button_frame,
            text="Close",
            command=format_window.destroy,
            style="Rounded.TButton",
            width=10,
        )
        close_button.pack(side=tk.LEFT, padx=5, expand=True)

        # نوار وضعیت (Status Bar)
        self.status_var = tk.StringVar(value="Ready")  # متن پیش‌فرض نوار وضعیت
        status_bar = ttk.Label(format_frame, textvariable=self.status_var, style="Status.TLabel")
        status_bar.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

    def start_format(self):
        # print("s")
        selected_usb = self.usb_var.get() 
        volume_label = self.volume_entry.get()
        file_system = self.file_system_var.get()
        quick_format = self.quick_format_var.get()

        
        self.status_var.set("Formatting... Please wait.")
        try:
            # print("s")
            self.disk.Format_Disk(selected_usb,file_system,volume_label)
            self.root.after(3000, lambda: self.status_var.set("Format completed successfully!"))
        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")
           

    def reset(self):
        self.root.destroy()
        DiskUI()


if __name__ == '__main__':
    DiskUI()