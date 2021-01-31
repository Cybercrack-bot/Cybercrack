import requests
from colorama import *
init()
red = Fore.RESET
reset = Fore.RED
def cookie():
    def help():
        print(r"""
    : set URL           target url to get the cookies
    : run or exploit    run the script
                            """)

    try:
        def get_cookies(url):
            session = requests.session()
            session.get(str(url))
            cookies = session.cookies
            for cookie in cookies:
                print(cookie)

        while True:
            try:
                user_in = input("CyberCrack: CyberServe/info/website_cookies > ")
                if user_in.startswith("set") and user_in.split()[1] == "URL":
                    url = str(user_in.split()[2])
                    print("URL = " + str(user_in.split()[2]))
                elif user_in == "run" or user_in == "exploit":
                    get_cookies(url=url)
                elif user_in == "help" or user_in == "show options":
                    help()
                else:
                    print(red + "Invalid command" + reset)
            except requests.exceptions.MissingSchema:
                print("Invalid url. please give the full url with https:// or http://")
            except requests.exceptions.InvalidSchema as e:
                print("The url you gave isn't valid")
                print(e)
            except requests.exceptions.ConnectionError:
                print("The target website closed the connection or can't connect to the target url")
            except NameError:
                print("[+] Assign all parameters related for this exploit")
    except Exception as e:
        print(e)