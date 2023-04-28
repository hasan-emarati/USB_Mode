# # # # import psutil
# # # # import wmi

# # # # c = wmi.WMI()
# # # # for disk in c.Win32_LogicalDisk():
# # # #     free_space = round(int(disk.FreeSpace)/(1024**3), 2) if disk.FreeSpace is not None else "-"
# # # #     size = round(int(disk.Size)/(1024**3), 2) if disk.Size is not None else "-"
# # # #     print(f"{disk.DeviceID}{disk.VolumeName}, Free Space: {free_space} GB, Size: {size} GB, File System: {disk.FileSystem},"
# # # #           f"serial Number: {disk.VolumeSerialNumber}")


# # # import psutil
# # # import wmi

# # # c = wmi.WMI()

# # # for disk in c.Win32_LogicalDisk():
# # #     free_space = round(int(disk.FreeSpace)/(1024**3), 2) if disk.FreeSpace is not None else "-"
# # #     size = round(int(disk.Size)/(1024**3), 2) if disk.Size is not None else "-"
# # #     read_only = "Read-only" if psutil.disk_partitions()[0].opts == "ro" else "Read/Write"
# # #     print(f"{disk.DeviceID}{disk.VolumeName}, Free Space: {free_space} GB, Size: {size} GB, File System: {disk.FileSystem},"
# # #           f"serial Number: {disk.VolumeSerialNumber}, {read_only}")




# # # class DiskInfo:
# # #     def refresh_disk_info(self):
# # #         c = wmi.WMI()
# # #         disk_info = ""
# # #         for disk in c.Win32_LogicalDisk():
# # #             free_space = round(int(disk.FreeSpace)/(1024**3), 2) if disk.FreeSpace is not None else "-"
# # #             size = round(int(disk.Size)/(1024**3), 2) if disk.Size is not None else "-"
# # #             disk_info += f"\n{disk.DeviceID}{disk.VolumeName} , Free Space: {free_space} GB , Size: {size} GB , File System: {disk.FileSystem} , serial Number: {disk.VolumeSerialNumber} \n"
# # #         return disk_info
    

# # import win32security
# # import ntsecuritycon as con
# # import getpass

# # file_name = r'H:\\' #THE USB


# # sd = win32security.GetFileSecurity(file_name, win32security.DACL_SECURITY_INFORMATION)
# # dacl = sd.GetSecurityDescriptorDacl()


# # ace_count = dacl.GetAceCount()
# # print('Ace count:', ace_count)

# # for i in range(0, ace_count):
# #     dacl.DeleteAce(0)


# # userx, domain, type = win32security.LookupAccountName("", "my.user")


# # dacl.AddAccessAllowedAceEx(win32security.ACL_REVISION, 3, 1179785, userx) # Read only


# # sd.SetSecurityDescriptorDacl(1, dacl, 0)   # may not be necessary
# # win32security.SetFileSecurity(file_name, win32security.DACL_SECURITY_INFORMATION, sd)
# import wmi
# c = wmi.WMI()
# disk_info = ""
# for disk in c.Win32_LogicalDisk():
#     if "Removable" in disk.Description:
#         free_space = round(int(disk.FreeSpace)/(1024**3), 2) if disk.FreeSpace is not None else "-"
#         size = round(int(disk.Size)/(1024**3), 2) if disk.Size is not None else "-"
#         disk_info += f"{disk.DeviceID}{disk.VolumeName} , Free Space: {free_space} GB , Size: {size} GB , File System: {disk.FileSystem}, VolumeDirty: {disk.VolumeDirty}, serial Number: {disk.VolumeSerialNumber}\n"
#         print (f"--------------------------------\n{disk_info}")

from tkinter import *
root = Tk()
v = IntVar()
Radiobutton(root, text='koskeshi', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='koni', variable=v, value=2).pack(anchor=W)
mainloop()
