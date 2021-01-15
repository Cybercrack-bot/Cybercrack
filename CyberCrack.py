#! /usr/bin/python3
from lib.common import shell
from lib.common import initalize
payloads = initalize.payloads
CyberServe = initalize.CyberServe
Cyber_Core = initalize.Cyber_Core
framework = shell.framework()
red = initalize.red
reset = initalize.reset
VERSION = "0.2"
try:
        import socket
        import random
        from Libraries import Cyber_Api as Cyber_Api
        import subprocess
        import time
        import colorama
        from colorama import Fore, Back, Style
        import optparse
        from Libraries import Cyber_Core as Cyber_Core
        parser = optparse.OptionParser()
        parser.add_option("-r", "--resource", help="Specify a resource file", dest="rc")
        (options, args) = parser.parse_args()
        framework()
except ImportError:
        print("[+] You haven't installed a module or haven't installed the tool completely. install it")
        quit()
except KeyboardInterrupt:
        print("[+] User aborted")




