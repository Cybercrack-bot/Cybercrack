from lib.common import shell
from lib.common import initalize
red = initalize.red
framework = shell.framework()
reset = initalize.reset
VERSION = "0.3"
import argparse
from Libraries import Cyber_setup
parser = argparse.ArgumentParser(
        add_help=False, description="[+] CyberCrack is a framework containing multiple tools.")
parser.add_argument(
        '-h', '-?', '--h', '-help', '--help', action="store_true",
        help=argparse.SUPPRESS)
parser.add_argument("--no-ascci", dest="ascci")
framework1 = parser.add_argument_group("[+] CyberCrack options")
framework1.add_argument('--update', action='store_true', help=' -                     Update the CyberCrack framework')
args = parser.parse_args()
if args.update:
    Cyber_setup.update()
elif args.h:
    parser.print_help()
else:
    shell.framework()
