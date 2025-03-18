import tkinter as tk
from tkinter import font
from tkinter import ttk
from ttkthemes import ThemedStyle
from USB import Disk
from tkinter import *
import re

class DiskUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Disk")
        self.style = ThemedStyle(self.root)
        self.style.set_theme("equilux")
        self.style = ttk.Style(self.style)
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.root.minsize(1050,150)
        self.root.maxsize(800,500)

        # Create an instance of Disk class
        self.disk_info = Disk()
        self.Eject = Disk()
        self.Format = Disk() 
        self.Read = Disk()
        self.Write = Disk()

        # Disk info label
        # self.disk_info_label = ttk.Label(self.frame, font=('Comic Sans MS', 15), anchor=tk.W, justify=tk.RIGHT)
        # self.disk_info_label.pack(fill=tk.BOTH, expand=True)

        # actions Button
        Data = self.disk_info.refresh_disk_info()
        regex = r"\n"
        matches = re.findall(regex, Data)
        counter = 0
        count = 5
        while counter < count :
            counter = counter + 1
            self.disk_info_label = ttk.Radiobutton(self.frame, variable=IntVar(), value=1 ,state='TLabel',)
            self.style.configure('TLabel', font=('Helvetica', 14))
            self.disk_info_label.pack(anchor=W,fill=tk.BOTH, expand=True)

        # Update button
        self.update_button = ttk.Button(self.frame, text="Update",state='', command=self.refresh_disk_info)
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

        # Refresh disk info on startup
        self.refresh_disk_info()
        # self.Eject_Disk()
        # self.Format_Disk()

        self.root.mainloop()

    def refresh_disk_info(self):
        disk_info = self.disk_info.refresh_disk_info()
        self.disk_info_label.config(text=f'   {disk_info}')

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























# from tkinter import *
# from tkinter import ttk

# #Create an instance of tkinter frame
# win = Tk()

# #Set the geometry of tkinter frame
# win.geometry("750x270")

# #Create an instance of Style Object
# style = ttk.Style()

# #Create ttk buttons
# small_button = ttk.Button(win, text="small button", style="small.TButton")
# small_button.pack(pady=20)

# big_button = ttk.Button(win, text="big button", style="big.TButton")
# big_button.pack()

# #Configure the properties of the Buttons
# style.configure('big.TButton', font=(None, 20), foreground="blue4")
# style.configure('small.TButton', font=(None, 7))

# win.mainloop()




# import tkinter as tk
# from tkinter import ttk
# from ttkthemes import ThemedStyle
# import psutil
# import wmi
# from USB import Disk


# import requests
# import tkinter as tk


# # #GUI Config
# # gui = tk.Tk()
# # gui.geometry('970x569')
# # gui.title("Zombs Royale Tools v1")
# # gui.resizable(False, False)

# # #Code below is the one i used to do this[![enter image description here][1]][1]
# # gui.overrideredirect(True) 


# # #Background-image
# # bgImage = tk.PhotoImage(file="width.png")
# # background_label = tk.Label(gui, image = bgImage)
# # background_label.place(x=0,y=0,relwidth=1, relheight=1)

# # #GUI Widgets#

# # #Exit Button
# # exit_image = tk.PhotoImage(file="close.gif")
# # exit_button = tk.Button(gui, image=exit_image, borderwidth=0, command=gui.destroy)
# # exit_button.place(rely=0.01, relx=0.01)



# # class DiskInfoUI:
# #     def __init__(self):
# #         self.root = tk.Tk()
# #         self.root.title("Disk")
# #         self.style = ThemedStyle(self.root)
# #         self.style.set_theme("equilux")
# #         self.frame = ttk.Frame(self.root, padding=10)
# #         self.frame.pack(fill=tk.BOTH, expand=True)

# #         # Disk info label
# #         self.disk_info_label = ttk.Label(self.frame, font=('Arial', 12), anchor=tk.W, justify=tk.LEFT)
# #         self.disk_info_label.pack(fill=tk.BOTH, expand=True)

# #         # Update button
# #         self.update_button = ttk.Button(self.frame, text="Update", command=self.refresh_disk_info)
# #         self.update_button.pack(side=tk.LEFT, padx=5, pady=10)

# #         # Exit button
# #         self.exit_button = ttk.Button(self.frame, text="Exit", command=self.root.destroy)
# #         self.exit_button.pack(side=tk.LEFT, padx=5, pady=10)

# #         # Create an instance of DiskInfo class
# #         self.disk_info = Disk()

# #         # Refresh disk info on startup
# #         self.refresh_disk_info()

# #         self.root.mainloop()

# #     def refresh_disk_info(self):
# #         disk_info = self.disk_info.refresh_disk_info()
# #         self.disk_info_label.config(text=disk_info)


# # if __name__ == '__main__':
# #     DiskInfoUI()




# class Disk_run:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Disk")
#         self.style = ThemedStyle(self.root)
#         self.style.set_theme("equilux")
#         self.frame = ttk.Frame(self.root, padding=10)
#         self.frame.pack(fill=tk.BOTH, expand=True)

#         # Disk info label
#         self.disk_info_label = ttk.Label(self.frame, font=('Arial', 12), anchor=tk.W, justify=tk.LEFT)
#         self.disk_info_label.pack(fill=tk.BOTH, expand=True)

#         # Update button
#         self.update_button = ttk.Button(self.frame, text="Update", command=self.refresh_disk_info)
#         self.update_button.pack(side=tk.LEFT, padx=5, pady=10)

#         # Exit button
#         self.exit_button = ttk.Button(self.frame, text="Exit", command=self.root.destroy)
#         self.exit_button.pack(side=tk.LEFT, padx=5, pady=10)

#         # Create an instance of Disk class
#         self.disk_info = Disk()

#         # Refresh disk info on startup
#         self.refresh_disk_info()

#         self.root.mainloop()

#     def refresh_disk_info(self):
#         disk_info = self.disk_info.refresh_disk_info()
#         self.disk_info_label.config(text=disk_info)

# if __name__ == '__main__':
#     Disk_run()
