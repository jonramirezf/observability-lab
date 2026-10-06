import psutil

cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

print(f"Uso de CPU: {cpu}%")
print(f"Uso de RAM: {ram}%")
print(f"Uso de disco: {disk}%")

if disk > 80:
    print("ADVERTENCIA: uso de disco alto")
