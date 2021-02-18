try:
    import requests
    from colorama import *
    from lib.functions.special_buitin_func import *
    init()
    red = Fore.RED
    green = Fore.GREEN
    reset = Fore.RESET
    def request(url):
        try:
            return requests.get("http://" + url)
        except requests.exceptions.ConnectionError:
            print(red + "[!] URL doesn't exist >> {} ".format(url) + reset)
            pass
        except KeyboardInterrupt:
            return
    def sending(url1, wordlist):
        try:
            with open(wordlist, "r") as wordlist:
                wordlist = wordlist.readlines()
                urls = []
                for phrase in wordlist:
                    phrase = phrase.strip()
                    url = url1 + "/" + phrase
                    response = request(url=url)
                    if response:
                        print(green + "[+] Discovered URL >> {}".format(url) + reset)
                        urls.append(url)
                    else:
                        coloured_print("[+] Url doesn't exist >> {}".format(url), colour=red)
                coloured_print("Here are the URLS. {}".format(list(urls)), green, auto_reset=False)
        except FileNotFoundError:
            no_such_file(wordlist)
        print(urls)
    def help():
        print(r"""
: set URL                The target url you want to brute_force. without http:// or https://
: set WORDLIST           The wordlist you want to use. there is a built in wordlist. located in the wordlists folder
: run or exploit         Run the script
: help                   show this message
        """)
    def console():
        while True:
            try:
                user_in = input("CyberCrack: CyberServe/brute_force/get_parameter > ")
                if user_in.startswith("set"):
                    if user_in.split()[1] == "URL":
                        url = user_in.split()[2]
                        print("URL = " + str(url))
                    elif user_in.split()[1] == "WORDLIST":
                        wordlist = user_in.split()[2]
                        print("WORDLIST = " + str(wordlist))
                    else:
                        print("[+] Invalid parameter for set")
                elif user_in.lower() == "help":
                    help()
                elif user_in.lower() == "run" or user_in.lower() == "exploit":
                    sending(wordlist=wordlist, url1=url)
                else:
                    no_such_command()
            except KeyboardInterrupt:
                break
            except NameError:
                fill_all()
except KeyboardInterrupt:
    print(red + "!! Exiting !!" + reset)