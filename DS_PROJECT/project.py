import shutil
import re
from os import system
import os
from random import *
import sys
import socket
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import webbrowser
import subprocess
import urllib.parse

os.system("clear")
# Call another Python program with arguments

subprocess.Popen(
    ['python3', '/Users/abhishekjhawar/Desktop/LABS/DS_LAB/PROJECT_DS_02/server.py']).wait(500)

subprocess.Popen(
    ['python3', '/Users/abhishekjhawar/Desktop/LABS/DS_LAB/PROJECT_DS_02/internal_s.py']).wait(300000)


file_path = "/Users/abhishekjhawar/Desktop/LABS/DS_LAB/PROJECT_DS_02/index.html"
webbrowser.get('chrome').open("file://" + file_path)
