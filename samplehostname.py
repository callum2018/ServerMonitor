import socket

def get_hostname():
    """Returns the hostname of the machine."""
    name = socket.gethostname()
    return name
