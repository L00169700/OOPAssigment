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
        
        ssh_stdin, ssh_stdout, ssh_stderr = session.exec_command("netstat -lntu", get_pty=True)     # To get all open ports
        is_ssh = False
        is_http = False
        for line in iter(ssh_stdout.readline, ""):
            print(line, end="")
            if (":22" in line and "LISTEN" in line):            # To check if 22 port is open
                is_ssh = True
            elif (":80" in line and "LISTEN" in line):          # To check if 80 port is open
                is_http = True

        if (is_ssh):
            print ("SSH")
        if (is_http):
            print ("HTTP")

        vm_output = connection.recv(65535)
        
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")

if __name__ == "__main__":
    #ssh_connection("192.168.1.103") #ip address of my VM, adjust to suit
    ssh_connection("192.168.1.103")
