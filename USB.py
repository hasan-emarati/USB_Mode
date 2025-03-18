import wmi
import subprocess
from notifypy import Notify

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
        for items in selected_items:
            item = items[:2]
            Command =f'(New-Object -comObject Shell.Application).Namespace(17).ParseName("{item}").InvokeVerb("Eject")'
            try:
                # Power Shell Commands
                result = subprocess.run(
                    ["powershell", "-Command", Command],
                    capture_output=True,
                    text=True,
                    shell=True
                )

                # Output 
                if result.stdout:
                    print("Output:", result.stdout)
                if result.stderr:
                    print("Error:", result.stderr)

                print(f"Drive {item} ejected successfully.")
                
                notification = Notify()
                notification.title = "Disk Safe to Eject"
                notification.message = "Eject successfully"
                notification.send() 
    
            except Exception as e:
                print(f"An error occurred: {e}")
        

    def Format_Disk(self, selected_items, SysFormat, Lable):
        drive = selected_items[:2]
        # print(drive)
        format_command = f'format {drive} /FS:{SysFormat} /Q /V:{Lable}'

        try:
            result = process = subprocess.Popen(
            format_command,
            stdin=subprocess.PIPE,  
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            text=True
        )
            process.stdin.write("\n") 
            process.stdin.flush()
            stdout, stderr = process.communicate()
            if stdout:
                print("Output:", stdout)
            if stdout:
                print("Output:", stderr)
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

        
    def Read_Only(self , selected_items):
        for items in selected_items:
            item = items[:1]
            # print(item)
            command1 = f"(echo select volume {item} & echo detail volume & echo list disk & echo attribute disk set readonly) | diskpart"
        process = subprocess.Popen(command1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        print(process)
        stdout, stderr = process.communicate(command1)
        print("stdout:", stdout)
        print("stderr:", stderr) 
        
    def Read_Write(self , selected_items):
        for items in selected_items:
            item = items[:1]
            # print(item)
            command1 = f"(echo select volume {item} & echo detail volume & echo list disk & echo attribute disk clear readonly) | diskpart"
        process = subprocess.Popen(command1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        print(process)
        stdout, stderr = process.communicate(command1)
        print("stdout:", stdout)
        print("stderr:", stderr)