import psutil

partitions = psutil.disk_partitions()

for partition in partitions:
    print(f"Device: {partition.device}, Mountpoint: {partition.mountpoint}, File system type: {partition.fstype}")
