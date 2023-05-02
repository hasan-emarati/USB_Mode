# import tkinter as tk
# from tkinter import ttk
# from ttkthemes import ThemedStyle
# from USB import Disk
# from tkinter import *
import wmi

# class DiskUI:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Disk")
#         self.style = ThemedStyle(self.root)
#         self.style.set_theme("equilux")
#         self.frame = ttk.Frame(self.root, padding=10)
#         self.frame.pack(fill=tk.BOTH, expand=True)
#         self.root.minsize(1000,150)
#         self.root.maxsize(800,500)
        
#         self.disk_info_label = ttk.Label(self.frame, font=('Arial', 12), anchor=tk.W, justify=tk.LEFT)
#         self.disk_info_label.pack(fill=tk.BOTH, expand=True)

#         self.update_button = ttk.Button(self.frame, text="Update", command=self.refresh_disk_info)
#         self.update_button.pack(side=tk.LEFT, padx=5, pady=10)

#         self.only_read_button = ttk.Button(self.frame, text="Only Read", command=self.refresh_disk_info)
#         self.only_read_button.pack(side=tk.LEFT, padx=5, pady=10)

#         self.read_write_button = ttk.Button(self.frame, text="Read/Write", command=self.refresh_disk_info)
#         self.read_write_button.pack(side=tk.LEFT, padx=5, pady=10)

#         self.format_button = ttk.Button(self.frame, text="Format", command=self.format_disk)
#         self.format_button.pack(side=tk.LEFT, padx=5, pady=10)

#         self.eject_button = ttk.Button(self.frame, text="Eject Disk", command=self.eject_disk)
#         self.eject_button.pack(side=tk.LEFT, padx=5, pady=10)

#         self.exit_button = ttk.Button(self.frame, text="Exit", command=self.root.destroy)
#         self.exit_button.pack(side=tk.RIGHT, padx=5, pady=10)

#         self.disk = Disk()
#         self.refresh_disk_info()

#         self.root.mainloop()

#     def refresh_disk_info(self):
#         disk_info = self.disk.refresh_disk_info()
#         self.disk_info_label.config(text=disk_info)

#     def eject_disk(self):
#         self.disk.eject_disk()

#     def format_disk(self):
#         self.disk.format_disk()

# if __name__ == '__main__':
#     DiskUI()



#Imports tkinter to create a window.
from tkinter import *
root=Tk()
root.title("BMI Calculator By")
  
#Creates Frames for items to go in.
topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)
  
#Creates labels to display how the app works.
theLabel = Label(topFrame, text="Body Mass Index also called BMI is used in the health industry")
theLabel.pack()
theLabel2 = Label(topFrame, text="to measure how over or underweight you are.")
theLabel2.pack()
theLabel3 = Label(topFrame, text="An ideal BMI ranges between 18.5 and 24.9.")
theLabel3.pack()
theLabel4 = Label(topFrame, text="bmi = weight /(height^2)*703")
theLabel4.pack()
theLabel5 = Label(topFrame, text="This is an example of someone who used our app.")
labelExamplename = Label(topFrame, text="Name = Boi")
labelExamplename.pack()
labelExampleheight = Label(topFrame, text="Height(in) = 69")
labelExampleheight.pack()
labelExampleweight = Label(topFrame, text="Weight(lb) = 160")
labelExampleweight.pack()
  
#Creates and displays variables to further display how it works.
name = "Boi"
height_in = 69
weight_lb = 160
bmi = weight_lb / (height_in ** 2)*703
labelExamplelabel = Label(topFrame, text="Boi's BMI is:")
labelExamplelabel.pack()
labelExample = Label(topFrame, text=bmi)
labelExample.pack()
  
#Entry Boxes and Labels for Height
LabelWhatisyourHeight = Label(topFrame, text="What is your height in inches?")
LabelWhatisyourHeight.pack()
Height = StringVar()
EntryBoxHeight = Entry(topFrame, textvariable=Height)
EntryBoxHeight.pack()
LabelWhatisyourHeightLabel = Label(topFrame, text="inches")
LabelWhatisyourHeightLabel.pack()
  
  
#Entry Boxes and Labels for Weight
LabelWhatisYourWeight = Label(topFrame, text="What is you Weight in pounds?")
LabelWhatisYourWeight.pack()
Weight = StringVar()
EntryBoxWeight = Entry(topFrame, textvariable=Weight)
EntryBoxWeight.pack()
LabelWhatisYourWeightLabel = Label(topFrame, text="pounds")
LabelWhatisYourWeightLabel.pack()
  
#Creates A Space
LabelNothing = Label(topFrame, text = "")
  
  
#Calculation Button (Figure out how to link this to a function
 
bmi = StringVar()
bmi.set("")
bmi2 = StringVar()
bmi2.set("")
 
def calculate():
    pounds = float(Weight.get())
    inches = float(Height.get())
    # labelYourBMI = Label(topFrame, text="Your BMI is")
    bmi.set("Your BMI is")
    labelYourBMI = Label(topFrame, textvariable=bmi)
    labelYourBMI.pack()
    bmi2.set((pounds) / (inches)**2*703)
    # bmitwo = (pounds) / (inches)**2*703
    labelYourBMI2 = Label(topFrame, textvariable=bmi2)
    labelYourBMI2.pack()
    return
  
ButtonCalculate = Button(topFrame, text="Calculate", command=calculate)
ButtonCalculate.pack()
  
#make sure to define the reset button
def reset():
    # labelYourBMI2 = Button(topFrame, text="")
    bmi.set("")
    bmi2.set("")
    Height.set('')
    Weight.set('')
    return
  
ButtonReset = Button(topFrame, text="Reset", command=reset)
ButtonReset.pack()
root.mainloop()