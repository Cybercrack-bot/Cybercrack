def phoneinfo(number):
    import time
    import phonenumbers
    from phonenumbers import carrier, geocoder, timezone
    phoneNumber = phonenumbers.parse(number)
    service = carrier.name_for_number(phoneNumber, 'en')
    region = geocoder.description_for_number(phoneNumber, 'en')
    valid = phonenumbers.is_valid_number(phoneNumber)
    possible = phonenumbers.is_possible_number(phoneNumber)
    timeZone = timezone.time_zones_for_number(phoneNumber)
    print(str(phoneNumber))
    time.sleep(1)
    print("Service: " + str(service))
    time.sleep(1)
    print("Region: " + str(region))
    time.sleep(1)
    print("Is the number valid: " + str(valid))
    time.sleep(1)
    print("Is it possible: " + str(possible))
    time.sleep(1)
    print("TimeZone: " + str(timeZone))
    time.sleep(1)


def help():
    print(r"""
set NUMBER       -       the phone number to find information. include the country code.
run or exploit   -       run the script
    """)
def console():
    global number
    while True:
        try:
            user_in = input("CyberCrack: CyberServe/info/phone_number > ").strip()
            if user_in.startswith("set") and user_in.split()[1] == "NUMBER":
                number = user_in.split()[2]
                print("NUMBER = " + str(number))
            elif user_in == "run" or user_in == "exploit":
                phoneinfo(number=number)
            elif user_in == "help" or user_in == "show options":
                help()
            else:
                print("Invalid command")
        except NameError:
            print("Assign all parameters related to this module")
        except KeyboardInterrupt:
            break

