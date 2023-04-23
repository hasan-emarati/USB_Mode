# # import psutil
# # import wmi

# # c = wmi.WMI()
# # for disk in c.Win32_LogicalDisk():
# #     free_space = round(int(disk.FreeSpace)/(1024**3), 2) if disk.FreeSpace is not None else "-"
# #     size = round(int(disk.Size)/(1024**3), 2) if disk.Size is not None else "-"
# #     print(f"{disk.DeviceID}{disk.VolumeName}, Free Space: {free_space} GB, Size: {size} GB, File System: {disk.FileSystem},"
# #           f"serial Number: {disk.VolumeSerialNumber}")


# import psutil
# import wmi

# c = wmi.WMI()

# for disk in c.Win32_LogicalDisk():
#     free_space = round(int(disk.FreeSpace)/(1024**3), 2) if disk.FreeSpace is not None else "-"
#     size = round(int(disk.Size)/(1024**3), 2) if disk.Size is not None else "-"
#     read_only = "Read-only" if psutil.disk_partitions()[0].opts == "ro" else "Read/Write"
#     print(f"{disk.DeviceID}{disk.VolumeName}, Free Space: {free_space} GB, Size: {size} GB, File System: {disk.FileSystem},"
#           f"serial Number: {disk.VolumeSerialNumber}, {read_only}")

import win32file
import win32api
import win32con

# ورودی کاربر
drive_letter = input("Enter the drive letter (e.g., D:): ")

# بررسی وضعیت دستگاه
try:
    # باز کردن فایل به صورت read-only
    file_handle = win32file.CreateFile(drive_letter, win32file.GENERIC_READ, win32file.FILE_SHARE_READ, None, win32file.OPEN_EXISTING, win32file.FILE_ATTRIBUTE_NORMAL, None)

    # دریافت اطلاعات ویژگی‌ها
    attributes = win32file.GetFileAttributes(drive_letter)

    # چک کردن وضعیت read-only
    if attributes & win32con.FILE_ATTRIBUTE_READONLY:
        print(f"The {drive_letter} drive is in read-only mode.")
    else:
        print(f"The {drive_letter} drive is not in read-only mode.")

    # چک کردن وضعیت دیگر ویژگی‌ها
    if attributes & win32con.FILE_ATTRIBUTE_DIRECTORY:
        print(f"The {drive_letter} drive is a directory.")
    else:
        print(f"The {drive_letter} drive is not a directory.")
    if attributes & win32con.FILE_ATTRIBUTE_ARCHIVE:
        print(f"The {drive_letter} drive is an archive.")
    else:
        print(f"The {drive_letter} drive is not an archive.")
    if attributes & win32con.FILE_ATTRIBUTE_HIDDEN:
        print(f"The {drive_letter} drive is hidden.")
    else:
        print(f"The {drive_letter} drive is not hidden.")
    if attributes & win32con.FILE_ATTRIBUTE_SYSTEM:
        print(f"The {drive_letter} drive is a system drive.")
    else:
        print(f"The {drive_letter} drive is not a system drive.")

    # بستن فایل
    win32file.CloseHandle(file_handle)

except Exception as e:
    print(f"Error: {e}")
