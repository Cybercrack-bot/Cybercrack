from lib.functions.special_buitin_func import *
import nmap
def recursive_dns_scan(host):
    try:
        import pprint
        pt = nmap.PortScanner()
        result = (pt.scan(hosts=host, arguments="-sU -p 53 --script=dns-recursion"))
        if (((result.get("nmap")).get("scaninfo")).get("error")):
            return "[+] The dns server is not valid"
        compare = ((((result.get('scan')).get(host)).get("udp")).get(53)).get("script")
        compare = str(compare)
        if compare == "None":
            return "[+] The dns server isn't valid"
        elif compare == "{'dns-recursion': 'Recursion appears to be enabled'}":
            return "[+] Dns recursion appears to be enabled"

    except KeyboardInterrupt:
        return "[+] Stopped"
    except AttributeError as e:
        return "[+] Dns recursion appears to be disabled"
    except ValueError:
        return "[+] No escape characters"



def help():
    print_help(r"""
: set DNS           The dns server you want to scan
: run or exploit    Run the script
    """)


def console():
    while True:
        try:
            user_in = input("CyberCrack: CyberServe/scanner/dns_recursion > ")
            user_in = user_in.lower()
            if user_in.lower() == "help" or user_in.lower() == "show options":
                help()
            elif user_in.startswith("set") and user_in.split()[1] == "dns":
                dns = user_in.split()[2]
                print("DNS = {}".format(dns))
            elif user_in == "run" or user_in == "exploit":
                print(recursive_dns_scan(dns))
            else:
                no_such_command()
        except KeyboardInterrupt:
            break
        except NameError:
            fill_all()



