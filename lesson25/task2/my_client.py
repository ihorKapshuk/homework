import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b"Hello, world|1", (HOST, PORT))
    data = s.recvfrom(1024)

print(f"Received {data!r}")