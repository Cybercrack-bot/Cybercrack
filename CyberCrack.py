import argparse
from Libraries import Cyber_setup
from lib.common import shell
framework = shell.framework()
VERSION = "0.5"
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
