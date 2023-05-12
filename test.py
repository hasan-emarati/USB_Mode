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
import tkinter as tk
import psutil
def init(self, num_buttons):
    self.num_buttons = num_buttons
    self.window = tk.Tk()
    self.window.title("صفحه با دکمه ها")
    # تعداد ستون‌ها برای grid
    self.num_columns = 5
    # ایجاد دکمه‌ها
    self.buttons = []
    drives = psutil.disk_partitions()
    for i in range(self.num_buttons):
        row = i // self.num_columns # شماره ردیف
        column = i % self.num_columns # شماره ستون
        if i < len(drives):
            drive = drives[i].device
        else:
            drive = ""
        button = tk.Button(self.window, text=drive, command=lambda i=i: self.button_click(i))
        button.grid(row=row, column=column)
        self.buttons.append(button)
    self.window.mainloop()
def button_click(self, index):
    print(f"دکمه {index + 1} فشرده شد")
# if __name__ == '__main__':
#     GUI()