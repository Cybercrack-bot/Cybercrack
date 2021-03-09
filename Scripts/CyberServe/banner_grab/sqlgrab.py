from lib.functions.special_buitin_func import *
def grab(ip):
    import socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, 3306))
    banner = server.recv(1024)
    return banner.decode()


def module_help():
    print(r"""
: set THOST        The target Ip address
: run or exploit   Run the script
    
    """)

def console():
    while True:
        try:
            user_in = input("CyberCrack: CyberServe/banner_grab/mysql_grab > ")
            if user_in == "help":
                module_help()
            elif user_in.startswith("set") and user_in.split()[1] == "THOST":
                ip = user_in.split()[2]
                print("THOST = " + ip)
            elif user_in == "run" or user_in == "exploit":
                grab(ip=ip)
            else:
                no_such_command()
        except NameError:
            fill_all()