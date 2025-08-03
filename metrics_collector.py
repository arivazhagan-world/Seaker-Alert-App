import psutil
import time
import platform

def get_metrics():
    boot_time = time.time() - psutil.boot_time()
    uptime_hours = round(boot_time / 3600, 2)

    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "ram_used_gb": round(psutil.virtual_memory().used / (1024 ** 3), 2),
        "ram_total_gb": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "disk_used_gb": round(psutil.disk_usage('/').used / (1024 ** 3), 2),
        "disk_total_gb": round(psutil.disk_usage('/').total / (1024 ** 3), 2),
        "uptime_hours": uptime_hours,
        "device": platform.node()
    }
