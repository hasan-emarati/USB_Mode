import wmi
class Disk:
    def refresh_disk_info(self):
        c = wmi.WMI()
        disk_info = []
        for disk in c.Win32_LogicalDisk():
            if "Removable" in disk.Description:
                free_space = round(int(disk.FreeSpace)/(1024**3), 2) if disk.FreeSpace is not None else "-"
                size = round(int(disk.Size)/(1024**3), 2) if disk.Size is not None else "-"
                disk_info += [f'{disk.DeviceID}{disk.VolumeName} Free Space: {free_space} GB Size: {size} GB File System: {disk.FileSystem} VolumeDirty: {disk.VolumeDirty} Serial Number: {disk.VolumeSerialNumber}']
        return disk_info
    
    def Eject_Disk(self):
        print("Disk is Ejecting")
        
    def Format_Disk(self):
        print("Formatting disk")
        
    def Read_Only(self):
        print("Read-Only")
        
    def Read_Write(self):
        print("Read/Write")
