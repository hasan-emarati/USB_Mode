# import psutil
import wmi

class Disk:
    def refresh_disk_info(self):
        c = wmi.WMI()
        disk_info = ""
        for disk in c.Win32_LogicalDisk():
            if "Removable" in disk.Description:
                free_space = round(int(disk.FreeSpace)/(1024**3), 2) if disk.FreeSpace is not None else "-"
                size = round(int(disk.Size)/(1024**3), 2) if disk.Size is not None else "-"
                disk_info += f"{disk.DeviceID}{disk.VolumeName} , Free Space: {free_space} GB , Size: {size} GB , File System: {disk.FileSystem} , serial Number: {disk.VolumeSerialNumber}\n"
        
        return disk_info
    
    def Eject_Disk(self):
        print("Disk is Ejecting")
        
        return
    
    def Format_Disk(self):
        print("Formatting disk")
        
        return 


# import wmi

# class Disk:
#     def __init__(self, device_id):
#         self.device_id = device_id
#         self.disk = self.get_disk_by_device_id(device_id)

#     def get_disk_by_device_id(self, device_id):
#         c = wmi.WMI()
#         disks = c.Win32_LogicalDisk()
#         for disk in disks:
#             if disk.DeviceID == device_id:
#                 return disk
#         return None

#     def refresh_disk_info(self):
#         self.disk = self.get_disk_by_device_id(self.device_id)

#     def get_free_space(self):
#         if self.disk.FreeSpace is None:
#             return "-"
#         return round(int(self.disk.FreeSpace)/(1024**3), 2)

#     def get_size(self):
#         if self.disk.Size is None:
#             return "-"
#         return round(int(self.disk.Size)/(1024**3), 2)

#     def get_file_system(self):
#         return self.disk.FileSystem

#     def get_serial_number(self):
#         return self.disk.VolumeSerialNumber

#     def eject_disk(self):
#         c = wmi.WMI()
#         disks = c.Win32_LogicalDisk()
#         for disk in disks:
#             if disk.DeviceID == self.device_id:
#                 disk.EjectMedia()
#                 return True
#         return False

#     def format_disk(self):
#         c = wmi.WMI()
#         disks = c.Win32_LogicalDisk()
#         for disk in disks:
#             if disk.DeviceID == self.device_id:
#                 result = disk.Format()
#                 if result[0] == 0:
#                     return True
#                 else:
#                     return False
#         return False





# import wmi

# class Disk:
#     def __init__(self):
#         self.c = wmi.WMI()

#     def refresh_disk_info(self, device_id=None):
#         disk_info = ""
#         for disk in self.c.Win32_LogicalDisk():
#             if "Removable" in disk.Description:
#                 if device_id is not None and device_id != disk.DeviceID:
#                     continue
#                 free_space = round(int(disk.FreeSpace)/(1024**3), 2) if disk.FreeSpace is not None else "-"
#                 size = round(int(disk.Size)/(1024**3), 2) if disk.Size is not None else "-"
#                 disk_info += f"{disk.DeviceID}{disk.VolumeName} , Free Space: {free_space} GB , Size: {size} GB , File System: {disk.FileSystem} , serial Number: {disk.VolumeSerialNumber}\n"
        
#         return disk_info
    
#     def Eject_Disk(self, device_id):
#         disk = self.c.Win32_LogicalDisk(DeviceID=device_id)
#         if len(disk) == 0:
#             return "Disk not found"
        
#         partition = disk[0].Associators()[0]
#         result, = partition.Win32_DiskDrive().Eject(True)
#         return "Disk ejected" if result == 0 else "Error ejecting disk"
    
#     def Format_Disk(self, device_id):
#         disk = self.c.Win32_LogicalDisk(DeviceID=device_id)
#         if len(disk) == 0:
#             return "Disk not found"
        
#         drive = disk[0].DeviceID.replace("\\", "")
#         result, = self.c.Win32_Volume(DriveLetter=drive).Format()
#         return "Disk formatted" if result == 0 else "Error formatting disk"
