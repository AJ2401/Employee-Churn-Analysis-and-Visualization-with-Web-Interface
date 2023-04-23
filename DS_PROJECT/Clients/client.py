import socket
from random import *
import os
import sys
from os import system
import shutil


max = 1024*1024

os.system("clear")
print("My IP : \n")
ip = socket.gethostbyname("localhost")
print('-----------------------------------------------------------------------------\n')
print(ip)
print('\n-----------------------------------------------------------------------------\n')
print("\n\n\n")


# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Taking input from Client which should match with Server input So that a port can generate
l = int(input('Enter Lower Limit :  \n'))
while l < 5:
    l = int(input('Retry !\nEnter Lower Limit :  \n'))


u = int(input('Enter Upper Limit : \n'))
while u < 25:
    u = int(input('Retry !\nEnter Upper Limit : \n'))

# hash Function to convert into a valid port
r = 1000*(u-l)+l

print("PORT" + str(r))
# Connect the socket to the server's IP address and port number
# ip = input("Enter the Ip address to Connect : \n\n")
server_address = ("192.168.1.3", r)
client_socket.connect(server_address)

n = 1
while n > 0:
    # Send the file name to the server
    file_name = input("Enter the Filename : \n")
    client_socket.sendall(file_name.encode())

    file_size = os.path.getsize(file_name)
    client_socket.sendall(str(file_size).encode('utf-8'))

    # Open the file for reading
    with open(file_name, 'rb') as file:
        # Send the file data to the server
        while True:
            data = file.read(max)
            if not data:
                break
            client_socket.sendall(data)
    n = n-1
# Close the connection
client_socket.close()
print('Connection closed')
