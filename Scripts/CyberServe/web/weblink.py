import requests
from colorama import *
init()
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
def link():
    GREEN = Fore.GREEN
    GRAY = Fore.LIGHTBLACK_EX
    RESET = Fore.RESET
    import re

    def crawl(url):
        url = url
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')

        urls = []
        for link in soup.find_all('a'):
            print(link.get('href'))

    def help():
        print(r"""
    : set URL                 the target ip
    : run or exploit          run the script
                            """)

    while True:
        try:
            user_in = input("CyberCrack: CyberServe/info/extract_web_links > ")
            if user_in == "help" or user_in == "show options":
                help()
            elif user_in.startswith("set"):
                ip = user_in.split()[2]
                if user_in.split()[1] == "URL":
                    print("URL = " + str(ip))
                else:
                    print("[+] Invalid parameter for set")
            elif user_in == "run" or user_in == "exploit":
                crawl(url=ip)
            else:
                print("[+] Invalid command")
        except NameError as e:
            print("[+] Assign all parameters related to this module ")
            print(e)
        except requests.exceptions.InvalidSchema:
            print("[+] Invalid URL")
        except requests.exceptions.MissingSchema:
            print("[+] Inculde https:// or http:// in the url")