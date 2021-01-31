from netaddr import *
def subnet():
    def help():
        print(r"""
    : set THOST           target ip to be tested
    : set NET             the network with the CIDR
    : run or exploit  run the script
                            """)
        return ""

    def net(ip, net):
        if IPAddress(ip) in IPNetwork(net):
            print("[+] The ip " + str(ip) + " is in the network " + str(net))
        else:
            print("[+] The ip " + str(ip) + " is not in the network " + str(net))

    while True:
        try:
            user_in = input("CyberCrack: Cyberserve/info/subnet_lookup > ")
            if user_in == "help" or user_in == "show options":
                help()
            elif user_in.startswith("set"):
                if user_in.split()[1] == "THOST":
                    ip = user_in.split()[2]
                    print("THOST = " + str(ip))
                elif user_in.split()[1] == "NET":
                    network = user_in.split()[2]
                    print("NET = " + str(network))
                else:
                    print("Invalid parameter for set")
            elif user_in == "run" or user_in == "exploit":
                net(ip=ip, net=network)
        except NameError:
            print("[+] Assign all values related to this module")