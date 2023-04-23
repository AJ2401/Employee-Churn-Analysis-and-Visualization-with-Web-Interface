# Age Analysis of Churn Rate in an Organisation
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import socket
import os
import sys
import subprocess
from os import system


os.system("clear")
port = 9000
# For Dynamic Port Allocation
# l = int(input('Enter Lower Limit :  \n'))
# while l < 5:
#     l = int(input('Retry !\nEnter Lower Limit :  \n'))


# u = int(input('Enter Upper Limit : \n'))
# while u < 25:
#     u = int(input('Retry !\nEnter Upper Limit : \n'))

# # hash Function to convert into a valid port
# r = 1000*(u-l)+l

# print("PORT" + str(r))


# Define server address and port
SERVER_ADDRESS = ('192.168.1.3', port)

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
client_socket.connect(SERVER_ADDRESS)


# Receive a text file from the server
file_name = "text.txt"
with open(file_name, "wb") as file:
    print(f"Receiving {file_name} from server...")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(data)
        file.write(data)
    print(f"{file_name} received successfully")
# Close the connection and the socket
client_socket.close()


with open("text.txt", "r") as file:
    # Read the contents of the file as a list of strings
    lines = file.readlines()

    # Search each line for the HTTPS link
    for line in lines:
        if "https://" in line:
            h = line.split("https://")[1].split()[0]
            break
    else:
        h = None

    # Print the HTTPS link
    if h:
        filename = "https://"+h
    else:
        print("No HTTPS link found in the file")

print(filename)

employee_churn = pd.read_csv(filename, index_col="Unnamed: 0")


# Create a KDE plot with a vertical line at the median age
sns.kdeplot(data=employee_churn, x="Age", fill=True)
# Constructing a Horizontal Line of Median
plt.axvline(employee_churn['Age'].median(), ymax=0.95, linestyle='--')


# Add text indicating the median age
plt.text(employee_churn['Age'].median() + 2, 0.04,
         'Median Age:' + str(employee_churn['Age'].median()))

# Remove the left spine of the plot
# making it a graph from a box
sns.despine(left=True)

# Set the x-label, y-ticks, and plot title
plt.xlabel('Employee Age', fontsize=12, fontweight='semibold')
# removing y scale
plt.yticks([])
plt.title('Age Distribution of Employees', fontsize=14, fontweight='semibold')

# Save the plot as a JPEG image
plt.savefig('1.jpg', dpi=400)

# Show the plot on the screen
subprocess.run(
    ['python3', '/Users/abhishekjhawar/Desktop/LABS/DS_LAB/PROJECT_DS_02/process/img_client.py', '1.jpg']).wait(500)


# plt.show()
exit(0)
