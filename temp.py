# import psutil
# import wmi

# c = wmi.WMI()
# for disk in c.Win32_LogicalDisk():
#     free_space = round(int(disk.FreeSpace)/(1024**3), 2) if disk.FreeSpace is not None else "-"
#     size = round(int(disk.Size)/(1024**3), 2) if disk.Size is not None else "-"
#     print(f"{disk.DeviceID}{disk.VolumeName}, Free Space: {free_space} GB, Size: {size} GB, File System: {disk.FileSystem},"
#           f"serial Number: {disk.VolumeSerialNumber}")


import psutil
import wmi

c = wmi.WMI()

for disk in c.Win32_LogicalDisk():
    free_space = round(int(disk.FreeSpace)/(1024**3), 2) if disk.FreeSpace is not None else "-"
    size = round(int(disk.Size)/(1024**3), 2) if disk.Size is not None else "-"
    read_only = "Read-only" if psutil.disk_partitions()[0].opts == "ro" else "Read/Write"
    print(f"{disk.DeviceID}{disk.VolumeName}, Free Space: {free_space} GB, Size: {size} GB, File System: {disk.FileSystem},"
          f"serial Number: {disk.VolumeSerialNumber}, {read_only}")
