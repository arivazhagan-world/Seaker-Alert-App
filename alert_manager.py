import json
from metrics_collector import get_metrics

def load_thresholds():
    with open("config.json", "r") as f:
        return json.load(f)

def check_alerts(metrics, thresholds):
    alerts = []
    if metrics['cpu_percent'] > thresholds['cpu_percent']:
        alerts.append(f"⚠️ High CPU Usage: {metrics['cpu_percent']}%")

    if metrics['ram_used_gb'] > thresholds['ram_used_gb']:
        alerts.append(f"⚠️ High RAM Usage: {metrics['ram_used_gb']} GB")

    if metrics['disk_used_gb'] > thresholds['disk_used_gb']:
        alerts.append(f"⚠️ High Disk Usage: {metrics['disk_used_gb']} GB")

    return alerts
