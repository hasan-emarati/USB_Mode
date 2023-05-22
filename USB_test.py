# # import subprocess

# # result = subprocess.run('wmic logicaldisk get caption', capture_output=True, text=True)


# # eject_cmd = f'rundll32.exe shell32.dll,Control_RunDLL hotplug.dll,I:'
# # subprocess.run(eject_cmd)

# import win32api
# import win32file
# import win32con
# import win32file
# import win32con

# drive_letter = "H"
# file_handle = win32file.CreateFile(
#     f"\\\\.\\{drive_letter}:",
#     win32con.GENERIC_WRITE,
#     0,
#     None,
#     win32con.OPEN_EXISTING,
#     win32con.FILE_ATTRIBUTE_READONLY,
#     None
# )

# win32api.CloseHandle(file_handle)

# import wmi

# drive_letter = "H"
# c = wmi.WMI()
# for logical_disk in c.Win32_LogicalDisk(DriveType=2):
#     if logical_disk.Caption.startswith(drive_letter):
#         logical_disk.Attributes |= 2
#         logical_disk.Put()

import wmi

drive_letter = "H"
c = wmi.WMI()
for logical_disk in c.Win32_LogicalDisk(DriveType=2):
    if logical_disk.Caption.startswith(drive_letter):
        logical_disk.Attributes &= ~2
        logical_disk.Put()