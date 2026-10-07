import psutil


def get_system_stats():
    cpu = psutil.cpu_percent(interval=None)
    memory = psutil.virtual_memory()
    storage = psutil.disk_usage("C:\\")

    return {
        "cpu": cpu,
        "ram": memory.percent,
        "storage": storage.percent,
    }