# It Represents the age Distribution amoung the Gender
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import socket
import subprocess
import os
import sys
from os import system

os.system("clear")
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
port = 9000

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


employee_churn = pd.read_csv(
    filename, index_col="Unnamed: 0")

employee_churn.tail()


# Making a Subset on males and compute their median age
male_churn = employee_churn[employee_churn['Gender'] == "Male"]
median_male_age = male_churn['Age'].median()

# Making a Subset on females and compute their median age
female_churn = employee_churn[employee_churn['Gender'] == "Female"]
median_female_age = female_churn['Age'].median()


# Set initial plot options
sns.set_style('white')

# Create figure and axes
# The figure has two rows and 1 column
# Will plot each subplot/axes on each row
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# Create plot of male age distribution on first axes
# making it to a Curve over the blocks / rows
sns.distplot(male_churn['Age'], color='skyblue', kde_kws={
             'shade': True}, hist=False, ax=axes[0])

# Add vertical line and annotate median age for male employees on first axes
axes[0].axvline(median_male_age, ymax=0.95, linestyle='--')
axes[0].text(median_male_age + 3, 0.04, 'Median Age:' + str(median_male_age))
axes[0].text(10, 0.04, str(male_churn.shape[0]) + ' employees')

# Add number of male employees for context
# Format subplot in first axes
axes[0].set_yticks([])
axes[0].set_xlabel('Male Employees', fontsize=12, fontweight='semibold')

# Create plot of female age distribution on second axes
sns.distplot(female_churn['Age'], color='red', kde_kws={
             'shade': True}, hist=False, ax=axes[1])

# Add vertical line and annotate median age for female employees on second axes
axes[1].axvline(median_female_age, ymax=0.95, linestyle='--')
axes[1].text(median_female_age + 3, 0.04,
             'Median Age:' + str(median_female_age))

# Add number of female employees for context
axes[1].text(10, 0.04, str(female_churn.shape[0]) + ' employees')
axes[1].set_yticks([])
axes[1].set_xlabel('Female Employees', fontsize=12, fontweight='semibold')
# Despine visualizations
sns.despine(left=True)
# Figure final formatting
fig.suptitle('Age distribution by gender', fontsize=14, fontweight='semibold')
plt.savefig('2.jpg', dpi=400)
# plt.show()
subprocess.run(
    ['python3', '/Users/abhishekjhawar/Desktop/LABS/DS_LAB/PROJECT_DS_02/process/img_client.py', '2.jpg']).wait(500)
exit(0)
