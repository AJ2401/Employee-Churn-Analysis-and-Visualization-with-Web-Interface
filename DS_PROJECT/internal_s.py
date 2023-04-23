import socket
import time
import subprocess
import os
n = 8
max_size = 1024
file_name = "text.txt"
port = 9000


pid = os.popen(f"lsof -ti :{port}").read().strip()
if pid:
    # Kill the process using the given PID
    os.system(f"kill {pid}")
    print(f"Process using port {port} has been killed (PID: {pid}).")
else:
    print(f"No process found using port {port}.")


# Define the server address
SERVER_ADDRESS = ('192.168.1.3', port)

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(SERVER_ADDRESS)

# Listen for incoming connections
server_socket.listen(n)

print(f"Server listening at {SERVER_ADDRESS}")

# Wait for 5 seconds to give the clients time to connect
print("Waiting for clients to connect...")
time.sleep(5)

for i in range(n):
    # Wait for a connection
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    # Send the text file to the client
    with open(file_name, 'rb') as file:
        while True:
            data = file.read(max_size)
            if not data:
                break
            client_socket.sendall(data)

    # Close the connection
    client_socket.close()

# Close the server socket
server_socket.close()

print("Connection closed")
