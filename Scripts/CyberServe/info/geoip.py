def geoloc():
    def geoip(ip):
        from geoip import geolite2
        match = geolite2.lookup(ip)
        print("Ip address - " + match.ip)
        print("Country - " + match.country)
        print("Continent - " + match.continent)
        print("Timezone - " + match.timezone)
        print("Location - " + str(match.location))

    while True:
        try:
            user_in = input("CyberCrack: CyberServe/info/geoip > ")
            if user_in == "help" or user_in == "show options":
                print(r"""
            : set THOST              The target ip address
            : run                    run the script
                                        """)
            elif user_in.startswith("set") and user_in.split()[1] == "THOST":
                ip = user_in.split()[2]
                print("THOST = " + str(ip))
            elif user_in == "run" or user_in == "exploit":
                geoip(ip=ip)
            else:
                print("[+] Invalid command")
        except NameError:
            print("[+] Assign al values related to this exploit")