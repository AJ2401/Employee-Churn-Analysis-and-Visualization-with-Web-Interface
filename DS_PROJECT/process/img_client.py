import socket
import sys
import os

host = '192.168.1.3'
port = 8090
image_name = sys.argv[1]  # Replace with the filename of the image to send

s = socket.socket()
print('[+] Client socket is created.')

s.connect((host, port))
print('[+] Socket is connected to {}'.format(host))

# Read the image file and send it over the network
with open(image_name, 'rb') as f:
    image_data = f.read()
    s.sendall(image_data)
    print('[+] {} is sent'.format(image_name))

s.close()
