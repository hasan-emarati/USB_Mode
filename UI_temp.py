import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import psutil
import wmi


import requests
import tkinter as tk


#GUI Config
gui = tk.Tk()
gui.geometry('970x569')
gui.title("Zombs Royale Tools v1")
gui.resizable(False, False)

#Code below is the one i used to do this[![enter image description here][1]][1]
gui.overrideredirect(True) 


#Background-image
bgImage = tk.PhotoImage(file="width.png")
background_label = tk.Label(gui, image = bgImage)
background_label.place(x=0,y=0,relwidth=1, relheight=1)

#GUI Widgets#

#Exit Button
exit_image = tk.PhotoImage(file="close.gif")
exit_button = tk.Button(gui, image=exit_image, borderwidth=0, command=gui.destroy)
exit_button.place(rely=0.01, relx=0.01)



# class DiskInfoUI:
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

#         # Create an instance of DiskInfo class
#         self.disk_info = DiskInfo()

#         # Refresh disk info on startup
#         self.refresh_disk_info()

#         self.root.mainloop()

#     def refresh_disk_info(self):
#         disk_info = self.disk_info.refresh_disk_info()
#         self.disk_info_label.config(text=disk_info)


# if __name__ == '__main__':
#     DiskInfoUI()




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
