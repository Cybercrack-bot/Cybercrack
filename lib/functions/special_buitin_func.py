from colorama import Fore
import socket


def coloured_print(string, colour, end="\n", auto_reset=False):
    from colorama import Fore, init
    init(autoreset=auto_reset)
    red = Fore.RED
    blue = Fore.BLUE
    green = Fore.GREEN
    yellow = Fore.YELLOW
    reset = Fore.RESET
    if colour == red:
        print(red + string + reset, end=end)
    elif colour == blue:
        print(blue + string + reset, end=end)
    elif colour == green:
        print(green + string + reset, end=end)
    elif colour == yellow:
        print(yellow + string + reset, end=end)


def fill_all():
    print_error("\n[+] Fill all the necessary parameters. type help for more info\n")
    return


def no_such_command():
    print(Fore.RED + "[+] Invalid command" + Fore.RESET)
    return


def no_such_file(file):
    print("[+] No such file named {}".format(str(file)))
    return


def print_error(string):
    print(Fore.RED + string + Fore.RESET)
    return


def print_status(string):
    print(Fore.GREEN + string + Fore.RESET)
    return


def print_help(string):
    print(Fore.GREEN + string + Fore.RESET)
    return


def invalid_set_pram():
    print_error("[+] Invalid parameter for set")
    return


def connect(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    return s


def print_success():
    print(Fore.BLUE + "[+] Execution completed" + Fore.RESET)
    return


def print_failure():
    print_error("[!] Execution failed")
    return


def print_result(result):
    print(Fore.BLUE + result + Fore.RESET)