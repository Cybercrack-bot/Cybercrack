import socket
import time
from lib.functions.special_buitin_func import *


def grab(ip):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print_status("[+] Socket created")
        time.sleep(1)
        server.connect((ip, 21))
        data = server.recv(1024)
        print_status("[+] " + data.decode())
        print_success()
    except socket.error:
        print_error("[+] Failed to create connection")
        print_failure()


def help():
    print_help(r"""
: set THOST               The target host
: run or exploit          Run the script 
    """)


def console():
    while True:
        try:
            user_in = input("CyberCrack: CyberServe/banner_grab/ftp_grab > ").strip()
            if user_in == "help" or user_in == "show options":
                help()
            elif user_in.startswith("set") and user_in.split()[1] == "THOST":
                thost = user_in.split()[2]
                print("THOST = " + str(thost))
            elif user_in == "run" or user_in == "exploit":
                grab(ip=thost)
            else:
                no_such_command()
        except NameError:
            fill_all()
        except KeyboardInterrupt:
            break
