import wmi
import subprocess

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
    
    def Eject_Disk(self, selected_items):
        for item in selected_items:
            eject_cmd = f'rundll32.exe shell32.dll,Control_RunDLL hotplug.dll,{item[:2]}'
            subprocess.run(eject_cmd)
            print(f"[{item[:2]}] is Ejecting")
        
    def Format_Disk(self , selected_items):
        for item in selected_items:
            Format_Disk = f'format {item[:2]} /FS:FAT32 /Q /V:MyUSB'
            subprocess.run(f"{Format_Disk}\n" , shell=True)
            print(f"[{item[:2]}] is Formatting")
        
    def Read_Only(self , selected_items):
        for item in selected_items:
            c = wmi.WMI()
            drive_letter = f"{item[:1]}"
            print(drive_letter)
            for logical_disk in c.Win32_LogicalDisk(DriveType=2):
                if logical_disk.Caption.startswith(drive_letter):
                    logical_disk.Attributes |= 2
                    logical_disk.Put()
                print(f"[{item[:2]}] is Read-Only mode")
        
    def Read_Write(self , selected_items):
        for item in selected_items:
            c = wmi.WMI()
            drive_letter = f"{item[:1]}"
            for logical_disk in c.Win32_LogicalDisk(DriveType=2):
                if logical_disk.Caption.startswith(drive_letter):
                    logical_disk.Attributes &= ~2
                    logical_disk.Put()

        print(f"[{item[:2]}] Read/Write")