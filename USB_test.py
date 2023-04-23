'''
Usage: python3 usb_eject.py
OS: Window7 and later
Eject the usb storage when the usb device plugin your PC!
'''
from time import sleep
import http.client
import subprocess

def monitorUSBStorage():
    label = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
    'T','U','V','W','X','Y','Z']
    monitorDisk = []
    for i in label:
        try:
            file = open(i+':/')
        except Exception as e:
            '''
            error = 2  =>not found
            error = 13 =>permission denied (exist!)
            '''
            if(e.errno == 13):
                print("Disk : "+i+" Exist!")
            else:
                monitorDisk.append(i)

    print("Start monitoring.....")
    while(True):
        print("Check...")
        isININ = False;
        disk = '';
        for i in monitorDisk:
            try:
                file = open(i+':/')
            except Exception as e:
                if(e.errno == 13):
                    print("Disk : "+i+" Exist!")
                    isININ = True
                    disk = i
                    break
        if(isININ):
            tmpFile = open('tmp.ps1','w')
            tmpFile.write('$driveEject = New-Object -comObject Shell.Application\n')
            tmpFile.write('$driveEject.Namespace(17).ParseName("'+disk+':").InvokeVerb("Eject")')
            tmpFile.close()
            process = subprocess.Popen(['powershell.exe', '-ExecutionPolicy','Unrestricted','./tmp.ps1'])
            process.communicate()
        #sleep for 2 seconds
        sleep(2)

if __name__ == '__main__':
    monitorUSBStorage()


# import psutil
# import wmi




# partitions = psutil.disk_partitions()
# for partition in partitions:
#     if "removable" in partition.opts:
#         print(f"{partition.device} is a removable drive")
#         try:
#             usage = psutil.disk_usage(partition.mountpoint)
#             print(f"Total space: {round(usage.total / (1024**3), 2)} GB, "
#                   f"Free space: {round(usage.free / (1024**3), 2)} GB, "
#                   f"Used space: {round(usage.used / (1024**3), 2)} GB")
#             read_write_info = psutil.disk_io_counters(perdisk=True).get(partition.device)
#             if read_write_info:
#                 print(f"Read count: {read_write_info.read_count}, "
#                       f"Write count: {read_write_info.write_count}, "
#                       f"Read bytes: {round(read_write_info.read_bytes / (1024**2), 2)} MB, "
#                       f"Write bytes: {round(read_write_info.write_bytes / (1024**2), 2)} MB")
#             else:
#                 print("No read/write info available")
#         except PermissionError:
#             print(f"No access permission to {partition.device}")
#         except FileNotFoundError:
#             print(f"{partition.device} does not exist")
#         print("------------------------") 