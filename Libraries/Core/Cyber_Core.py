from colorama import *
init()
from Scripts.Payloads import windowsrevtcp, wifipass, webcampayload
from Scripts.Exploits import shellshock, fuzz
from Scripts.CyberServe.web import websitesql, webpagesql, weblink, webcookie, browsercookie
from Scripts.CyberServe.info import geoip, subnet, whois, phoneinfo
from Scripts.CyberServe.spoof import arpspoof
from Scripts.CyberServe.scanner import portscanbyserv, portscan
from Scripts.CyberServe.brute_force import cracksql
from scapy.all import *
red = Fore.RED
reset = Fore.RESET
class cybercrack:
        class payloads:
            def __init__(self):
                junk = "Get"
            def windows_cybershell_rev_tcp(self):
                windowsrevtcp.shell()
            def Cybercrack_wifi_password(self):
                wifipass.wifipass()
            def spy_webcam_snap(self):
                webcampayload.console()

        class modules:
            class exploits:
                def shellshock(self):
                    shellshock.shellshock()
                def Fuzzer(self):
                    fuzz.fuzzer()
            class CyberServe:
                def CyberServe_scanner_scan_host_byserv(self):
                    portscanbyserv.scanp()
                def CyberServe_scanner_sql_vulnerability(self):
                    websitesql.websitesql()
                def Cyberserve_scanner_webpage_sql_vulnerabilty(self):
                    webpagesql.webpagesql()
                def CyberServe_info_browser_cookies(self):
                    browsercookie.cookie()
                def CyberServe_scanner_ports(self):
                    portscan.scan()
                def Cyberserve_info_website_cookies(self):
                    webcookie.cookie()
                def Cyberserve_spoof_arp_spoof(self):
                    arpspoof.arp_spoof()
                def CyberServe_info_phone(self):
                    phoneinfo.console()
                def Cyberserve_info_subnet_lookup(self):
                    subnet.subnet()
                def Cyberserve_info_whois_lookup(self):
                    whois.whois()
                def CyberServe_info_extract_weblinks(self):
                    weblink.link()
                def CyberServe_info_geoip(self):
                    geoip.geoloc()
                def CyberServe_brute_force_sql_crack(self):
                    cracksql.console()
