VERSION = "0.1"
try:
    from Libraries import Cyber_Core
    from Libraries import Cyber_Api
    from colorama import *
    red = Fore.RED
    reset = Fore.RESET
    init()
    payloads = Cyber_Core.cybercrack.payloads
    modules = Cyber_Core.cybercrack.modules
    exploits = modules.exploits
    CyberServe = modules.CyberServe
    Cyber_Api.initialize()
except ImportError:
    print("[+] You haven't installed a module or haven't installed the tool completely. install it")
    quit()
except KeyboardInterrupt:
    print("[+] User aborted")
