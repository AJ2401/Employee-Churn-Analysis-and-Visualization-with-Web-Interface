# Server Which Recieves File From the Client
import socket
from random import *
import subprocess
import os
import sys
from os import system
import re
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
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


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


# Bind the socket to a specific IP address and port number
server_address = ("192.168.1.3", r)
server_socket.bind(server_address)


# Listen for incoming connections
server_socket.listen(5)

# Wait for a connection
print('Waiting for a connection...')
connection, client_address = server_socket.accept()
print('Connected by', client_address)
# Receive the file name
file_name = connection.recv(max).decode()
file_size = int(connection.recv(1024).decode('utf-8'))
print('Received file size:', file_size)

with open("text.txt", 'wb') as file:
    # Receive the file data
    received_data = 0
    while received_data < file_size:
        data = connection.recv(1024)
        received_data += len(data)
        file.write(data)
    # Close the connection
os.rename(file_name, "text.txt")
connection.close()
sys.exit(0)
