try:
    import socket
    from colorama import *
    init()
    def scanp():
        def help():
           print(r"""
        : set THOST       the target ip
        : set SERVICE     the service(s) you want to check. if the services are more than one use , to seperate and don't use blanks. eg :- ftp,http,https,etc.
        : run or exploit  run the script
           """)
        def isopen(host, port):
            s = socket.socket()
            try:
                s.connect((host, port))
            except:
                return False
            else:
                return True

        def scan(servlist, host):
            yellow = Fore.YELLOW
            reset = Fore.RESET
            gray = Fore.LIGHTBLACK_EX
            red = Fore.RED
            if "," in servlist:
                for service in servlist.split(","):
                    try:
                        portNum = socket.getservbyname(service, "tcp")
                        if isopen(host=host, port=int(portNum)):
                            print(yellow + "[+] The service " + service + " is running on port " + str(portNum) + " and it's open" + reset)
                        else:
                            print(gray + "[+] The service " + service + " running on port " + str(portNum) + " and it is closed" + reset)
                    except OSError:
                        print(red + "[+] The service " + str(service) + " doesn't exist" + reset)
                        continue
                else:
                    print(yellow + "[+] Finished scanning" + reset)

            else:
                try:
                    portNum = socket.getservbyname(servlist, "tcp")
                    if isopen(host=host, port=int(portNum)):
                        print(Fore.YELLOW + "[+] The service " + servlist + " is running on port " + str(portNum) + " and it's open" + Fore.RESET)
                    else:
                        print(Fore.LIGHTBLACK_EX + "[+] The service " + servlist + " running on port " + str(portNum) + " and it is closed" + Fore.RESET)
                except OSError:
                    print(red + "[+] The service " + str(servlist) + " doesn't exist" + reset)

        while True:
            try:
                user_in = input("CyberCrack: CyberServe/scanner/scan_host_by_serv > ")
                if user_in == "help" or user_in == "show options":
                    help()
                elif user_in.startswith("set"):
                    if user_in.split()[1] == "SERVICE":
                        if "," in user_in.split()[2]:
                            serv = user_in.split()[2]
                            print("SERVICE = " + str(serv))
                        else:
                            serv = user_in.replace("set SERVICE ", "")
                            print("SERVICE = " + str(serv))
                    elif user_in.split()[1] == "THOST":
                        host = user_in.split()[2]
                        print("THOST = " + str(host))
                    else:
                        print("Invalid parameter for set")
                elif user_in == "run" or user_in == "exploit":
                    scan(servlist=serv, host=host)
                else:
                    print("Invalid command")
            except KeyboardInterrupt:
                break
            except NameError:
                print("[+] Assign all parameters related to his module")
            except EOFError:
                continue

except KeyboardInterrupt:
    print("Quiting")
