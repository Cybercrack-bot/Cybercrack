from Libraries.Core import Cyber_Core
loaded_payloads = Cyber_Core.cybercrack.payloads
loaded_CyberServe = Cyber_Core.cybercrack.modules.CyberServe
loaded_exploits = Cyber_Core.cybercrack.modules.exploits
from lib.common.initalize import *
r"""
    :   CyberServe/scanner/tcp_ports                 Scan all the ports to find open tcp ports
    :   CyberServe/info/whois_lookup                 Give you the whois lookup of the target ip
    :   CyberServe/info/extract_web_links            Extract the links from the target website 
    :   CyberServe/info/geoip                        Give you the location of the target ip
    :   CyberServe/info/subnet_lookup                Check if a ip is in a network
    :   CyberServe/info/browser_cookies              List all the cookies in the target web browser
    :   CyberServe/scanner/website_sql_vulnerability Scan for sql vulnerabilities on the target website 
    :   CyberServe/scanner/webpage_sql_vulnerability Scan for sql vulnerabilities on the target webpage
    :   CyberServe/info/website_cookies              Get the cookies from the target url
    :   CyberServe/spoof/arp_spoof                   Arp spoof
    :   CyberServe/scanner/scan_host_by_serv         Scan target host and check if the given service name is available
    :   CyberServe/brute_force/sql_login             Brute force sql login
        """
class redirector:
    def __init__(self):
        version = "0.4"
        from Libraries.Core import Cyber_Core
    def redirector_modules(self, option):
        if option == "CyberServe/scanner/tcp_ports":
            loaded_CyberServe.CyberServe_scanner_ports(self=red)
        elif option == "CyberServe/info/whois_lookup":
            loaded_CyberServe.Cyberserve_info_whois_lookup(self=red)
        elif option == "CyberCrack/exploits/fuzzer":
            loaded_exploits.Fuzzer(self=red)
        elif option == "CyberServe/info/extract_web_links":
            loaded_CyberServe.CyberServe_info_extract_weblinks(self=red)
        elif option == "CyberServe/info/geoip":
            loaded_CyberServe.CyberServe_info_geoip(self=red)
        elif option == "CyberServe/info/subnet_lookup":
            loaded_CyberServe.Cyberserve_info_subnet_lookup(self=red)
        elif option == "CyberServe/info/browser_cookies":
            loaded_CyberServe.CyberServe_info_browser_cookies(self=red)
        elif option == "CyberServe/scanner/website_sql_vulnerability":
            loaded_CyberServe.CyberServe_scanner_sql_vulnerability(self=red)
        elif option == "CyberServe/scanner/webpage_sql_vulnerability":
            loaded_CyberServe.Cyberserve_scanner_webpage_sql_vulnerabilty(self=red)
        elif option == "CyberServe/info/website_cookies":
            loaded_CyberServe.Cyberserve_info_website_cookies(self=red)
        elif option == "CyberServe/spoof/arp_spoof":
            loaded_CyberServe.Cyberserve_spoof_arp_spoof(self=red)
        elif option == "CyberServe/scanner/scan_host_by_serv":
            loaded_CyberServe.CyberServe_scanner_scan_host_byserv(self=red)
        elif option == "CyberServe/brute_force/sql_login":
            loaded_CyberServe.CyberServe_brute_force_sql_crack(self=red)
        elif option == "CyberCrack/exploits/shellshock":
            loaded_exploits.shellshock(self=red)
        elif option == "CyberServe/info/phone_number":
            loaded_CyberServe.CyberServe_info_phone(self=red)
        else:
            print("[+] No such module or exploit")
    def redirector_payloads(self, payload, command):
        if payload == "windows/CyberShell/rev_tcp":
            loaded_payloads.windows_cybershell_rev_tcp(self=red)
        elif payload == "malware/wifi/password":
            loaded_payloads.Cybercrack_wifi_password(self=red)
        elif payload == "spy/webcam/snap":
            loaded_payloads.spy_webcam_snap(self=red)
        else:
            print("[+] There is no payload in the framework called " + command.split()[2])