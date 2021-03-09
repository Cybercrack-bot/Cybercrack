def grab(lport, lhost):
    import socket
    import time
    s = socket.socket()
    s.connect((lhost, lport))
    print("[+] Connection made")
    time.sleep(1)
    print("[+] Waiting for banner")
    banner = s.recv(1048576).decode()
    time.sleep(1)
    if banner is None:
        print("[+] The banner received is empty")
        return
    else:
        print("[+] Banner received successfully")
        print("\n" + banner)
        return


def help():
    print(r"""
: set THOST           The target host you want to grab the banner from 
: run or exploit      Run the script
    """)
def console():
    while True:
        try:
            user_in = input("CyberCrack: CyberServe/banner_grab/ssh > ").strip()
            if user_in == "help" or user_in == "show options":
                help()
            elif user_in.startswith("set") and user_in.split()[1] == "THOST":
                lhost = user_in.split()[2]
                print("THOST = " + str(lhost))
            elif user_in == "run" or user_in == "exploit":
                grab(lhost=lhost, lport=int(22))
            else:
                print("[+] Invalid command")
        except KeyboardInterrupt:
            break
        except NameError:
            print("[+] Assign all values related to this module")
