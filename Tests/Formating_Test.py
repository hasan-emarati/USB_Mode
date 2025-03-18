# اطلاعات چند دیسک به‌صورت یک لیست از رشته‌ها
disk_info = [
    "H:MYUSB Free Space: 7.48 GB Size: 7.48 GB File System: FAT32 VolumeDirty: False Serial Number: 5C0C1903",
    ]

# نمایش دو حرف اول هر رشته (حرف درایو)
for disk in disk_info:
    drive_letter = disk[:2]  # استخراج دو حرف اول
    print(drive_letter)




# subprocess.run(format_command, shell=True, check=True, text=True, capture_output=True) 