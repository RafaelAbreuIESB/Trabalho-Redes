import os

# Configurações principais
SERVER_IP = "127.0.0.1"
WINDOW_SECONDS = int(os.getenv("WINDOW_SECONDS", 5))
API_HOST = "0.0.0.0"
API_PORT = 8000
CAPTURE_INTERFACE = "Software Loopback Interface 1"
