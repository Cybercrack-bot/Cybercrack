import socket
from colorama import *
init()
red = Fore.RED
reset = Fore.RESET
def scan():
    while True:
        try:
            PortScannerInput = input("CyberCrack: CyberServe/scanner/tcp_ports > ")
            if "set THOST " in PortScannerInput:
                ip_2 = PortScannerInput.replace("set THOST ", "")
                print("THOST = " + str(ip_2))


            elif PortScannerInput == "show options" or PortScannerInput == "Show options":
                def options():
                    print(r"""
                   USAGE                         example
            : set THOST 'targetip'     example 'set LHOST 192.168.1.4'
            : set SCAN_TILL            the port you wamt to scan till
            : run or exploit           example 'run'
                                      """)
                    return ""

                options()
            elif PortScannerInput.startswith("set") and PortScannerInput.split()[1] == "SCAN_TILL":
                port_till = PortScannerInput.split()[2]
                print("SCAN_TILL = " + str(port_till))
            elif PortScannerInput == "run" or PortScannerInput == "exploit":
                try:
                    host = ip_2
                    RESET = reset
                    GRAY = Fore.LIGHTBLACK_EX
                    GREEN = Fore.GREEN

                    def is_port_open(host, port):
                        s = socket.socket()
                        try:
                            s.connect((host, port))
                        except:
                            return False
                        else:
                            return True

                    for port in range(1, int(port_till)):
                        if is_port_open(host, port):
                            print(f"{GREEN}[+] {host}:{port} is open  - {RESET}" + socket.getservbyport(port, "tcp"))
                        else:
                            print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")
                except KeyboardInterrupt:
                    print("\n Exitting Program !!!!")
                    break
                except socket.gaierror:
                    print("\n Hostname Could Not Be Resolved !!!!")
                    break
                except socket.error:
                    print("\ Server not responding !!!!")
                    break
            else:
                print(red + "Invalid Syntax" + reset)
        except NameError:
            print(red + "Assign all values and parameters" + reset)