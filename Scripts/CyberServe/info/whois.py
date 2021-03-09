from pprint import pprint
from ipwhois import IPWhois
def whois():
    def help():
        print(r"""
    : set THOST                         Type the target ip address
    : run or exploit                    run the script
    : Main()                            return to the main shell
                                        as simple as that
                            """)
        return ""

    def whois_look(ip):
        domain = IPWhois(ip)
        result = domain.lookup_whois()
        pprint(result)

    while True:
        input_user = input("CyberCrack: CyberServe/information/whois_lookup > ").strip()
        if input_user == "help" or input_user == "show options":
            help()
        elif input_user.startswith("set"):
            parameter = input_user.split()[1]
            if parameter == "THOST":
                ip_addr = input_user.split()[2]
                print("THOST = " + str(ip_addr))
            else:
                print("[+] Invalid parameter for set")
        elif input_user == "run" or input_user == "exploit":
            try:
                print("[+] This operation may take a few minutes")
                whois_look(ip=ip_addr)
            except NameError:
                print("[+] Assign all parameters related to this module")
        elif input_user == "Main()":
            break
        elif input_user == "":
            continue
        else:
            print("[+] Invalid syntax")