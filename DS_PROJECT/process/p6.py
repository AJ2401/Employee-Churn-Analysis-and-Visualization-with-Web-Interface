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


# Set initial plot options
sns.set_style('white')

# Create helper lists
survey_columns = ["EnvironmentSatisfaction",
                  "JobSatisfaction", "JobInvolvement", "WorkLifeBalance"]
survey_titles = ["Environment Satisfaction",
                 "Job Satisfaction", "Job Invovlvement", "Work-life Balance"]

# Create subplots - 2 rows, 2 columns
fig, axes = plt.subplots(2, 2, figsize=(24, 16))

# For every element
for ax, survey_question, title in zip(axes.flatten(), survey_columns, survey_titles):

    # Cross tabulate data and generate proportions for ecah survey question
    proportions = pd.crosstab(employee_churn[survey_question],
                              employee_churn['Attrition'],
                              normalize='index').reset_index()

    # Find percentages instead of proportions
    proportions[['Churned', 'Stayed']
                ] = proportions[['Churned', 'Stayed']] * 100

    # Get total column for each survey question
    proportions['Total'] = proportions['Churned'] + proportions['Stayed']

    # Plot Total plot
    sns.barplot(x='Total', y=survey_question, data=proportions, order=[
                'Low', 'Good', 'Great', 'Excellent'], color='g', ax=ax)

    # Plot Churned plot
    sns.barplot(x='Churned', y=survey_question, data=proportions, order=[
                'Low', 'Good', 'Great', 'Excellent'], color='r', ax=ax)

    # Despine plot
    sns.despine(left=True, bottom=True)
    # Set final formatting
    ax.set_title('Attrition by '+title, fontsize=14, fontweight='semibold')
    ax.set_xlabel('Attrition Rate ()', fontsize=12, fontweight='semibold')
    ax.set_ylabel(title, fontsize=12, fontweight='semibold')
plt.savefig('6.jpg', dpi=400)
# plt.show()
subprocess.run(
    ['python3', '/Users/abhishekjhawar/Desktop/LABS/DS_LAB/PROJECT_DS_02/process/img_client.py', '6.jpg']).wait(500)
exit(0)
