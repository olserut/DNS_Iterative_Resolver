import socket
import sys
import os

#serverName = sys.argv[1]
#DNS_IP = sys.argv[2]


serverName = "my.fiu.edu"
bytesToSend = str.encode(serverName)
serverAddressPort = ("198.41.0.4", 53)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(5.0)

s.sendto(bytesToSend, serverAddressPort)

print('Waiting...')

try:
    receivedBytes, addr = s.recvfrom(2048)
    print(receivedBytes[0].decode())
except socket.timeout:
    print('REQUEST TIMED OUT')


# py Desktop\mydns.py
