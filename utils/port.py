import socket

def isPortOpen(host, port):
    try:
        with socket.create_connection((host, port), timeout=5) as sock:
            return True
    except (socket.timeout, socket.error):
        return False