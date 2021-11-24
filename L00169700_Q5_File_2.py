"""
# 
# File : L00169700_Q5_File_2.py
# Created ：24.11.21
# Author ：R.Lima
# Version ：v1.0.0
# Licencing : (C) 2021 R.Lima, LYIT
# Available under GNU Public License (GPL)
# Description ：Manipulated the given code, create folders and subfolders.
"""

import paramiko
import time
import re

# Open SSH connection to the device
# first install ssh-server on the VM
# sudo apt install openssh-server openssh-client

def ssh_connection(ip):
    try:
        username = "L00169700"
        password = "Pass@#1234"

        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)
        print ("Connected to VM")
        connection = session.invoke_shell()
        connection.send("ls -al > longList.txt\n") #unix command to list directory contents and save to file
        time.sleep(1)

        session.exec_command("sudo apt install curl", get_pty=True)     # To install the curl
        session.exec_command("mkdir Labs")                              # To create the main folder "Labs" in home
        session.exec_command("mkdir Labs/Lab1")                         # To create the sub folder "Lab1" inside Labs folder
        session.exec_command("mkdir Labs/Lab2")                         # To create the sub folder "Lab2" inside Labs folder
        
        ssh_stdin, ssh_stdout, ssh_stderr = session.exec_command("ls -l --time=atime", get_pty=True)    # to find out when files were last accessed.

        for line in iter(ssh_stdout.readline, ""):
            print(line, end="")
   
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")

if __name__ == "__main__":
    #ssh_connection("192.168.1.103") #ip address of my VM, adjust to suit
    ssh_connection("192.168.1.103")
