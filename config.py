import os
#172.27.2.88
#192.168.56.1
# Configurações principais
SERVER_IP = "172.27.2.88"
WINDOW_SECONDS = int(os.getenv("WINDOW_SECONDS", 5))
API_HOST = "0.0.0.0"
API_PORT = 8000
CAPTURE_INTERFACE = "Software Loopback Interface 1"
