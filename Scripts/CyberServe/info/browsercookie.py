import browser_cookie3
def cookie():
    while True:
        try:
            user_in = input("CyberCrack: CyberServe/info/browser_cookies > ").strip()
            if user_in == "help" or user_in == "show options":
                print(r"""
    : set BROWSER     -      the target browser. eg- 'firefox, chrome, opera, microsoft-edge'
    : run or exploit  -      run the script
                """)
            elif user_in.startswith("set") and user_in.split()[1] == "BROWSER":
                if user_in.split()[2] == "firefox":
                    print("Browser = firefox")
                    browser = "firefox"
                elif user_in.split()[2] == "microsoft-edge":
                    print("Browser = microsoft-edge")
                    browser = "edge"
                elif user_in.split()[2] == "opera":
                    print("Browser = opera")
                    browser = "opera"
                elif user_in.split()[2] == "chrome":
                    print("Browser = chrome")
                    browser = "chrome"
                else:
                    print("[+] Invalid browser")
            elif user_in == "run" or user_in == "exploit":
                if browser == "firefox":
                    cookie = list(browser_cookie3.firefox())
                    for cookies in cookie:
                        print(cookies)
                elif browser == "edge":
                    cookie = list(browser_cookie3.edge())
                    for cookies in cookie:
                        print(cookies)
                elif browser == "opera":
                    cookie = list(browser_cookie3.opera())
                    for cookies in cookie:
                        print(cookies)
                elif browser == "chrome":
                    cookie = list(browser_cookie3.chrome())
                    for cookies in cookie:
                        print(cookies)
        except KeyboardInterrupt:
            quit()
        except NameError:
            print("[+] Assign all parameters related for this module")
        except browser_cookie3.BrowserCookieError:
            print("[+] The browser you specified isn't installed on your device")