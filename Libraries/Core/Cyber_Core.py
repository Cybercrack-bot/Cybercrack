from colorama import *
init()
from Scripts.Payloads import windowsrevtcp, wifipass, webcampayload
from Scripts.Exploits import shellshock, get_based_buffer_overflow
from Scripts.CyberServe.info import geoip, subnet, whois, phoneinfo, weblink, webcookie, browsercookie
from Scripts.CyberServe.spoof import arpspoof
from Scripts.CyberServe.scanner import portscanbyserv, portscan, webpagesql, websitesql, recursive_dns_scan
from Scripts.CyberServe.banner_grab import banner_grab, http_grab, ssh_grab, ftp_grab, sqlgrab
from Scripts.CyberServe.brute_force import cracksql, brute_force_get_parameter
from Scripts.CyberServe.scanner.wordpress import wordpress
from Scripts.CyberServe.osint.username import username_find
red = Fore.RED
reset = Fore.RESET
class cybercrack:
        class payloads:
            def __init__(self):
                __version__ = "0.5"

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
                    get_based_buffer_overflow.fuzzer()
            class CyberServe:
                def CyberServe_banner_grab_ssh(self):
                    ssh_grab.console()
                def CyberServe_banner_grab_http(self):
                    http_grab.console()
                def CyberServe_banner_grab_grab(self):
                    banner_grab.console()
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
                def CyberServe_scanner_recursive_dns(self):
                    recursive_dns_scan.console()
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
                def CyberServe_brute_force_get_parameter(self):
                    brute_force_get_parameter.console()
                def CyberServe_scanner_wordpress_version(self):
                    wordpress.console()
                def CyberServe_banner_grab_ftp_grab(self):
                    ftp_grab.console()
                def CyberServe_osint_username(self):
                    username_find.console()
                def CyberServe_banner_grab_mysql_grab(self):
                    sqlgrab.console()
