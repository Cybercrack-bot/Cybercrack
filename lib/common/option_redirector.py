from Libraries.Core import Cyber_Core
loaded_payloads = Cyber_Core.cybercrack.payloads
loaded_CyberServe = Cyber_Core.cybercrack.modules.CyberServe
loaded_exploits = Cyber_Core.cybercrack.modules.exploits
from lib.functions.special_buitin_func import *
from lib.common.initalize import *
from exceptions.Errors import *
cyberserve_dict = {
    "CyberServe/scanner/tcp_ports": loaded_CyberServe.CyberServe_scanner_ports,
    "CyberServe/info/whois_lookup": loaded_CyberServe.Cyberserve_info_whois_lookup,
    "CyberServe/info/extract_web_links": loaded_CyberServe.CyberServe_info_extract_weblinks,
    "CyberServe/info/geoip": loaded_CyberServe.CyberServe_info_geoip,
    "CyberServe/info/subnet_lookup": loaded_CyberServe.Cyberserve_info_subnet_lookup,
    "CyberServe/info/browser_cookies": loaded_CyberServe.CyberServe_info_browser_cookies,
    "CyberServe/scanner/website_sql_vulnerability": loaded_CyberServe.CyberServe_scanner_sql_vulnerability,
    "CyberServe/scanner/webpage_sql_vulnerability": loaded_CyberServe.Cyberserve_scanner_webpage_sql_vulnerabilty,
    "CyberServe/info/website_cookies": loaded_CyberServe.Cyberserve_info_website_cookies,
    "CyberServe/spoof/arp_spoof": loaded_CyberServe.Cyberserve_spoof_arp_spoof,
    "CyberServe/scanner/scan_host_by_serv": loaded_CyberServe.CyberServe_scanner_scan_host_byserv,
    "CyberServe/brute_force/sql_login": loaded_CyberServe.CyberServe_brute_force_sql_crack,
    "CyberServe/info/phone_number": loaded_CyberServe.CyberServe_info_phone,
    "CyberServe/banner_grab/grabber": loaded_CyberServe.CyberServe_banner_grab_grab,
    "CyberServe/banner_grab/ssh": loaded_CyberServe.CyberServe_banner_grab_ssh,
    "CyberServe/banner_grab/http": loaded_CyberServe.CyberServe_banner_grab_http,
    "CyberServe/brute_force/get_parameter": loaded_CyberServe.CyberServe_brute_force_get_parameter,
    "CyberServe/scanner/wordpress/version": loaded_CyberServe.CyberServe_scanner_wordpress_version,
    "CyberServe/banner_grab/ftp_grab": loaded_CyberServe.CyberServe_banner_grab_ftp_grab,
    "CyberServe/osint/username": loaded_CyberServe.CyberServe_osint_username,
    "CyberServe/banner_grab/mysql_grab": loaded_CyberServe.CyberServe_banner_grab_mysql_grab,
    "CyberServe/scanner/dns_recursion": loaded_CyberServe.CyberServe_scanner_recursive_dns
}
exploits_dict = {
    "get/web_server/buffer-overflow": loaded_exploits.Fuzzer,
    "CyberCrack/exploits/shellshock": loaded_exploits.shellshock
}
payloads_dict = {
    "windows/CyberShell/rev_tcp": loaded_payloads.windows_cybershell_rev_tcp,
    "spy/webcam/snap": loaded_payloads.spy_webcam_snap,
    "malware/wifi/password": loaded_payloads.Cybercrack_wifi_password
}



class redirector:
    def __init__(self):
        version = "0.4"


    def redirector_modules(self, option):
        try:
            if option in cyberserve_dict or option in exploits_dict:
                if option in cyberserve_dict:
                    cyberserve_dict.get(option, lambda: None)(self=red)
                elif option in exploits_dict:
                    exploits_dict.get(option, lambda: None)(self=red)
            else:
                raise ToolNotFoundError
        except ToolNotFoundError:
            print_error("[+] No such module or exploit")
        except IndexError:
            print_error("[+] Specify targets and parameters")


    def redirector_payloads(self, payload, command):
        try:
            if payload in payloads_dict:
                payloads_dict.get(payload, lambda: None)(self=red)
            else:
                raise PayloadNotFoundError
        except PayloadNotFoundError:
            print_error("[+] There is no payload in the framework called " + command.split()[2])
        except IndexError:
            print_error("[+] Specify targets and parameters")

class search:
    def search(self, option, types="all"):
        result = []
        if types == "all":
            print_status("\n[+] Here is the result of your qwery\n")
            for cyberserve in cyberserve_dict:
                if option in cyberserve:
                    result.append(cyberserve)
                else:
                    continue

            for payload in payloads_dict:
                if option in payload:
                    result.append(payload)
                else:
                    continue

            for exploit in exploits_dict:
                if option in exploit:
                    result.append(exploit)
                else:
                    continue
            if len(result) == 0:
                print_error("[!] No module called {}".format(option))
            else:
                for r in result:
                    print_result(r)
        elif types == "payloads":
            for payload in payloads_dict:
                if option in payload:
                    print_status("[+] Here is the result of your qwery\n")
                    result.append(payload)
                else:
                    continue

            if len(result) == 0:
                print_error("[!] No module called {}".format(option))
            else:
                for r in result:
                    print_result(r)
        elif types == "CyberServe":
            for cyberserve in cyberserve_dict:
                if option in cyberserve:
                    print_status("[+] Here is the result of your qwery\n")
                    result.append(cyberserve)
                else:
                    continue
            if len(result) == 0:
                print_error("[!] No module called {}".format(option))
            else:
                print_status("\n[+] Here is the result of your qwery\n")
                for r in result:
                    print_result(r)

        elif types == "exploits":
            for exploit in exploits_dict:
                if option in exploit:
                    print_status("[+] Here is the result of your qwery\n")
                    result.append(exploit)
                else:
                    continue
            if len(result) == 0:
                print_error("[!] No module called {}".format(option))
            else:
                for r in result:
                    print_result(r)

