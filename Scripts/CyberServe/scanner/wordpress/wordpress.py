import requests
import re
from lib.functions.special_buitin_func import *


def wordpress(url):
    r = requests.get(url)
    info = re.search('(<meta\sname="generator"\scontent=)(.*)',r.text)
    info = info.group(0)
    info = info.replace('<meta name="generator" content="WordPress ', "")
    version = info.replace('" />', "")
    return version


def check_version(url):
    try:
        return requests.get(url + "/wp-login.php")
    except requests.exceptions.MissingSchema:
        print_error("[+] The url must have http:// or https:// parameters")


def initialize(url):
    if check_version(url):
        print_status("[+] The site {} uses wordpress. retrieving version, please wait".format(url))
        version = wordpress(url)
        print_status("[+] The wordpress version of the website {} is {}".format(url, version))
        vulnerable(version)
    else:
        print_error("[+] The website {} doesn't have wordpress".format(url))


def vulnerable(version):
    vuln_versions = ["3.4.2", "3.5", "3.5.1"]
    if version == vuln_versions[0]:
        print_status("[+] 12 Vulnerabilities found in version 3.4.2")
    if version == vuln_versions[1]:
        print_status("[+] 10 Vulnerabilities found in version 3.4.2")
    if version == vuln_versions[2]:
        print_status("[+] 08 Vulnerabilities found in version 3.4.2")
    else:
        return


def help():
    print_help(r"""
: set URL            The target url. but remove / in the end of url. example, https://google.com not https://google.com/
: run or exploit     Run the script
    """)


def console():
    try:
        while True:
            try:
                user_in = input("CyberCrack: CyberServe/scanner/wordpress/version > ").strip()
                if user_in.startswith("set"):
                    if user_in.split()[1] == "URL":
                        url = user_in.split()[2]
                        print("URL = " + str(url))
                    else:
                        invalid_set_pram()
                elif user_in == "run" or "exploit":
                    initialize(url=url)
                elif user_in == "help" or user_in == "show options":
                    help()
                else:
                    no_such_command()
            except NameError:
                fill_all()
            except KeyboardInterrupt:
                return
    except NameError:
        fill_all()
    except KeyboardInterrupt:
        return