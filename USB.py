import psutil
import wmi

class DiskInfo:
    def refresh_disk_info(self):
        c = wmi.WMI()
        disk_info = ""
        for disk in c.Win32_LogicalDisk():
            if "Removable" in disk.Description:
                free_space = round(int(disk.FreeSpace)/(1024**3), 2) if disk.FreeSpace is not None else "-"
                size = round(int(disk.Size)/(1024**3), 2) if disk.Size is not None else "-"
                disk_info += f"\n{disk.DeviceID}{disk.VolumeName} , Free Space: {free_space} GB , Size: {size} GB , File System: {disk.FileSystem} , serial Number: {disk.VolumeSerialNumber}\n"
        return disk_info
    

# class DiskInfo:
#     def refresh_disk_info(self):
#         c = wmi.WMI()
#         disk_info = ""
#         for disk in c.Win32_LogicalDisk():
#             free_space = round(int(disk.FreeSpace)/(1024**3), 2) if disk.FreeSpace is not None else "-"
#             size = round(int(disk.Size)/(1024**3), 2) if disk.Size is not None else "-"
#             disk_info += f"\n{disk.DeviceID}{disk.VolumeName} , Free Space: {free_space} GB , Size: {size} GB , File System: {disk.FileSystem} , serial Number: {disk.VolumeSerialNumber} \n"
#         return disk_info
    
