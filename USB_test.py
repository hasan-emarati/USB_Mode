

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