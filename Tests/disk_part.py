import re

# متن ورودی
text = """
  Disk ###  Status         Size     Free     Dyn  Gpt
  --------  -------------  -------  -------  ---  ---
* Disk 2    Online           58 GB      0 B

Read-only              : No
Hidden                 : No
No Default Drive Letter: No
Shadow Copy            : No
Offline                : No
BitLocker Encrypted    : No
Installable            : Yes

Volume Capacity        :   58 GB
Volume Free Space      :   58 GB
"""

# الگوی Regex برای پیدا کردن عدد جلوی Disk
pattern = r"\* Disk (\d+)\s+Online"

# جستجو با Regex
match = re.search(pattern, text)

# اگر عدد پیدا شد، آن را چاپ کنید
if match:
    disk_number = match.group(1)
    print(f"Disk Number: {disk_number}")
else:
    print("Disk number not found.")