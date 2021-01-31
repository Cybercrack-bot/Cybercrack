from lib.common import shell
from lib.common import initalize
payloads = initalize.payloads
CyberServe = initalize.CyberServe
Cyber_Core = initalize.Cyber_Core
framework = shell.framework()
red = initalize.red
reset = initalize.reset
VERSION = "0.3"
import argparse
from Libraries import Cyber_setup
parser = argparse.ArgumentParser(
        add_help=False, description="[+] CyberCrack is a framework containing multiple tools.")
parser.add_argument(
        '-h', '-?', '--h', '-help', '--help', action="store_true",
        help=argparse.SUPPRESS)
framework = parser.add_argument_group("[+] CyberCrack options")
framework.add_argument('--update', action='store_true', help=' -                     Update the CyberCrack framework')
args = parser.parse_args()
if args.update:
    Cyber_setup.update()
elif args.h:
    parser.print_help()
else:
    framework()