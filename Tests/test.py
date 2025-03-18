# import tkinter as tk

# class GUI:
#     def init(self, num_buttons):
#         self.num_buttons = num_buttons
#         self.window = tk.Tk()
#         self.window.title("صفحه با دکمه ها")

#         # ایجاد دکمه‌ها
#         self.buttons = []
#         for i in range(self.num_buttons):
#             button = tk.Button(self.window, text=f"دکمه {i+1}", command=lambda i=i: self.button_click(i))
#             button.pack()
#             self.buttons.append(button)

#         self.window.mainloop()

#     def button_click(self, index):
#         print(f"دکمه {index + 1} فشرده شد")

# GUI()
# # [2:14 PM]
# import tkinter as tk

# class GUI:
#     def init(self, num_buttons):
#         self.num_buttons = num_buttons
#         self.window = tk.Tk()
#         self.window.title("صفحه با دکمه ها")

#         # تعداد ستون‌ها برای grid
#         self.num_columns = 5

#         # ایجاد دکمه‌ها
#         self.buttons = []
#         for i in range(self.num_buttons):
#             row = i // self.num_columns # شماره ردیف
#             column = i % self.num_columns # شماره ستون
#             button = tk.Button(self.window, text=f"دکمه {i+1}", command=lambda i=i: self.button_click(i))
#             button.grid(row=row, column=column)
#             self.buttons.append(button)

#         self.window.mainloop()

#     def button_click(self, index):
#         print(f"دکمه {index + 1} فشرده شد")

# if __name__ == '__main__':
#     GUI()
# [2:16 PM]
# import tkinter as tk
# import psutil
# def init(self, num_buttons):
#     self.num_buttons = num_buttons
#     self.window = tk.Tk()
#     self.window.title("صفحه با دکمه ها")
#     # تعداد ستون‌ها برای grid
#     self.num_columns = 5
#     # ایجاد دکمه‌ها
#     self.buttons = []
#     drives = psutil.disk_partitions()
#     for i in range(self.num_buttons):
#         row = i // self.num_columns # شماره ردیف
#         column = i % self.num_columns # شماره ستون
#         if i < len(drives):
#             drive = drives[i].device
#         else:
#             drive = ""
#         button = tk.Button(self.window, text=drive, command=lambda i=i: self.button_click(i))
#         button.grid(row=row, column=column)
#         self.buttons.append(button)
#     self.window.mainloop()
# def button_click(self, index):
#     print(f"دکمه {index + 1} فشرده شد")
# # if __name__ == '__main__':
# #     GUI()



from shutil import copytree as ct
from shutil import copyfile as cf
from shutil import make_archive as arc
from shutil import rmtree as rm
from time import sleep as wait

f_drive = r'F:\BACKUP\stuff'
path_to_user = r'path'
another_path = r"path"
a_path = r'path'

def backup():
    ct(r'path', r'path')
    ct(r'path', r"F:\\BACKUP\\stuff\\path")
    ct(r'path', r"path")
    ct(r'D:\\path', r'path')

print("Starting backup...")
print("This process is automatic. This should not take any longer than 2 minutes...")
backup()
print()
print("Backup complete!")
print("Archiving folder...")
arc(r"F:\BACKUP", "zip", r'F:\BACKUP')
rm(r'F:\BACKUP')
print("Program will close in 10 seconds.")
wait(10)
