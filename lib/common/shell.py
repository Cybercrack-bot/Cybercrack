from colorama import *
from exceptions.Errors import *
from lib.functions.special_buitin_func import *
import sys
init()
red = Fore.RED
def framework():

    try:
        def show_options():
            print(r"""
        :  options             show options related to the exploit or the payload
        :  payloads            show the current payloads
        :  exploits            show the current exploits
        :  CyberServe          show current CyberServe modules
            """)
            return ""

        def use_options():
            print(r"""
        :  Use                     it is used to use a exploit or a CyberServe module and you cant use it with payloads.
        type show exploits or show CyberServe to get a list of all the available payloads
            """)
            return ""
        def set_options():
            print(r"""
        :   set payload            set the payload to the payload of your choice
            """)

        def commands():
            print(r"""
        : show                 show the current options, payloads, CyberServe or exploits. type show for more info
        : load all             type this before you start using the framework. It loads the payloads, CyberServe and exploits
        : exit                 exit the framework
        : use                  use a exploit or a CyberServe. You can't use it with payloads
        : set                  use it to set parameters such as payload, LHOST, LPORT, etc.
        : help                 display this message
         """)
            return ""


        def exploits():
            print(r"""
        :   get/web_server/buffer-overflow    get request based web server fuzzer and show you the range where the overflow occur
        :   CyberCrack/exploits/shellshock    exploit shellshock vulnerability   
            """)
            return ""

        def payloads():
            print(r"""
        :   windows/CyberShell/rev_tcp        when the target execute the payload a CyberShell will spawn. It is like the meterpreter
        session
        :   malware/wifi/password             when the target execute the payload a CyberSession will spawn and you can get the password
        of any interface the target connected in the past and the current connected wifi
        :   spy/webcam/snap                   take pictures from the target and deliver then to you
            """)
            return ""

        def cyberserve():
            print(r"""
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
        :   CyberServe/info/phone_number                 Find information reguarding phone numbers
        :   CyberServe/banner_grab/grabber               Grab the banner from the port of your choice
        :   CyberServe/banner_grab/ssh                   Grab the banner from port 22 which is ssh
        :   CyberServe/banner_grab/http                  Grab the banner from port 80 which is http
        :   CyberServe/brute_force/get_parameter         Brute force get parameter
        :   CyberServe/scanner/wordpress/version         Get the wordpress version of the target website
        :   CyberServe/banner_grab/ftp_grab              Grab the banner from port 21 which is ftp
        :   CyberServe/osint/username                    An osint investigation to discover usernames
            """)
            return ""

        def shell():
            print(r"""
                                                         0 payloads loaded
                                                         0 exploits loaded
                                                         0 CyberServe loaded
                                                 Type load all to load all the tools
               """)
            while True:
                try:
                    command = input("\nCyberCrack > ").strip()
                    if command.startswith("show"):
                        if len(command.split()) == 1:
                            show_options()
                            continue
                        elif len(command.split()) == 2:
                            option = command.replace("show ", "")
                            if option == "options":
                                commands()
                                continue
                            elif option == "exploits":
                                exploits()
                                continue
                            elif option == "payloads":
                                payloads()
                                continue
                            elif option == "CyberServe":
                                cyberserve()
                                continue
                            else:
                                print("[+] Invalid parameter for 'show' type 'show' for more info")
                                continue
                        else:
                            if command.split()[1] == "options" or command.split()[1] == "exploits" or command.split()[1] == "payloads" or command.split()[1] == "CyberServe":
                                print("[+] Command '" + command.split()[1] + "' doesn't take any arguments")
                            else:
                                print("[+] Invalid parameter for the 'show' command")
                    elif command == "load all":
                        try:
                            loaded = "False"
                            from Libraries.Core import Cyber_Core
                            from lib.common import option_redirector
                            print("                       3  - payloads loaded")
                            print("                       2  - exploit loaded")
                            print("                       20 - CyberServe loaded")
                            print_status("              out of 25 Tools all are available")
                            loaded = "True"
                        except ImportError:
                            print_error(
                                "[+] Error occurred while importing the required modules.")
                    elif command.startswith("use"):
                        if len(command.split()) == 1:
                            use_options()
                        elif len(command.split()) == 2:
                            option = command.replace("use ", "")
                            try:
                                if loaded == "False":
                                    print('bye')
                                elif loaded == "True":
                                    option_redirector.redirector.redirector_modules(self=red, option=option)
                            except NameError:
                                print_error(
                                    "[+] The framework can't use anything because the modules are not loaded. Type 'load all' to ")
                                print_error("load the modules")
                    elif command.startswith("set"):
                        if len(command.split()) == 1:
                            set_options()
                        elif len(command.split()) == 2:
                            option = command.replace("set ", "")
                            if option == "payload":
                                print("[+] Type the payload of your choice")
                            else:
                                print("[+] Invalid parameter for 'set'")
                        elif len(command.split()) == 3:
                            try:
                                if loaded == "True":
                                    if command.split()[1] == "payload":
                                        payload = command.split()[2]
                                        option_redirector.redirector.redirector_payloads(self=red, payload=payload, command=command)
                                    else:
                                        print("[+] Invalid parameter for set. type 'set' for more info")
                                elif loaded == "False":
                                    print("bye")
                            except NameError:
                                print_error(
                                    "[+] The framework can't use anything because the modules are not loaded. Type 'load all' to ")
                                print_error("load the modules")
                        else:
                            print("[+] Invalid amount of arguments")
                    elif command == "exit":
                        quit()
                    elif command == "":
                        continue
                    elif command == "help":
                        commands()
                    elif command == "update":
                        update_complete = False
                        import subprocess
                        import platform
                        input("Hit enter to continue >> ")
                        if platform.system() == 'Windows':
                            subprocess.call("git reset --hard", shell=True)
                            subprocess.call("sudo git pull", shell=True)
                            print_success()

                        elif platform.system() == 'Linux':
                            subprocess.call("git reset --hard", shell=True)
                            subprocess.call("sudo git pull", shell=True)
                            print_success()

                        else:
                            subprocess.call("git reset --hard", shell=True)
                            subprocess.call("sudo git pull", shell=True)
                            print_success()
                        update_complete = True
                        input("Hit enter to finish >> ")
                        sys.exit("[+] Reinstall the requirements.txt")
                    elif command.startswith("search"):
                        if "type: " in command:
                            option_redirector.search.search(self=red, option=command.split([1], types=command.split()[3]))
                        else:
                            option_redirector.search.search(self=red, option=command.split()[1])
                    else:
                        try:
                            import subprocess
                            op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                            output = op.stdout.read()
                            output_error = op.stderr.read()
                            if output_error.decode():
                                raise CommandNotFoundError
                            else:
                                import os
                                os.system(command)
                        except CommandNotFoundError:
                            print_error("[+] Invalid command, {}".format(command))

                except KeyboardInterrupt:
                    print("!! Type exit to quit !!")

        shell()
    except IndexError:
        print_error("[!] Complete the command")

    except UnboundLocalError:
        print_error("[!] Some commands require this command, load all. execute that to avoid errors")
