import socket
from string import ascii_uppercase as all_upper

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def make_caesar(your_data):
    ciphered_str = []
    your_data = [*str(your_data)]
    your_data.remove("b")
    your_data.remove("'")
    your_data.remove("'")
    your_data = "".join(your_data).split("|")
    your_str = your_data[0]
    key = int(your_data[1])
    for letter in list(your_str.upper()):
        index = all_upper.find(letter) + key
        if index < 0:
            ciphered_str.append(all_upper[len(all_upper) + index])
        elif index >= len(all_upper):
            ciphered_str.append(all_upper[index - len(all_upper)])
        else:
            ciphered_str.append(all_upper[index])
    return "".join(ciphered_str).encode("utf-8")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    data, addr = s.recvfrom(1024)
    s.sendto(make_caesar(data),addr)