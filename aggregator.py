from collections import defaultdict
import threading

lock = threading.Lock()
# The traffic_data will now accumulate indefinitely
traffic_data = defaultdict(lambda: {"in": 0, "out": 0, "protocols": defaultdict(lambda: {"in": 0, "out": 0})})

def add_packet(client_ip, direction, size, proto):
    """Adds a packet to the cumulative traffic data."""
    with lock:
        traffic_data[client_ip][direction] += size
        traffic_data[client_ip]["protocols"][proto][direction] += size

def get_snapshot():
    """Returns a snapshot of the cumulative traffic data."""
    with lock:
        # The 'window_start' is no longer relevant
        return {
            "clients": dict(traffic_data)
        }