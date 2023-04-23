import socket
import os

host = '192.168.1.3'
port = 8090
buffer_size = 4096  # Adjust as necessary

s = socket.socket()
print('[+] Server socket is created.')

s.bind((host, port))
print('[+] Socket is bound to {}:{}'.format(host, port))

s.listen(1)
print('[+] Listening for incoming connections...')
i = 1
while True:
    conn, addr = s.accept()
    print('[+] New connection from {}'.format(addr))

    # Read the image data from the socket and save it to a file
    with open('{}.jpg'.format(i), 'wb') as f:
        while True:
            data = conn.recv(buffer_size)
            if not data:
                break
            f.write(data)

    print('[+] Image data received and saved to file.')
    i = i+1
    conn.close()
