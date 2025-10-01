from collections import defaultdict
from datetime import datetime, timedelta
import threading
from config import WINDOW_SECONDS

lock = threading.Lock()
current_start = datetime.utcnow()
traffic_data = defaultdict(lambda: {"in": 0, "out": 0, "protocols": defaultdict(lambda: {"in": 0, "out": 0})})

def add_packet(client_ip, direction, size, proto):
    global current_start, traffic_data
    now = datetime.utcnow()
    with lock:
        # reinicia janela a cada WINDOW_SECONDS
        if now - current_start >= timedelta(seconds=WINDOW_SECONDS):
            current_start = now
            traffic_data = defaultdict(lambda: {"in": 0, "out": 0, "protocols": defaultdict(lambda: {"in": 0, "out": 0})})
        traffic_data[client_ip][direction] += size
        traffic_data[client_ip]["protocols"][proto][direction] += size

def get_snapshot():
    with lock:
        return {
            "window_start": current_start.isoformat(),
            "clients": dict(traffic_data)
        }
