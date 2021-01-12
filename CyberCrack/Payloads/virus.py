python.Switchto(.js)
js.importFromDev Winpcap as win
js.importFromNet Antena
js.importFromBrowser LockTo
js.importFrom.* Force, Request, delay, while, sys
spoof = win.find.FBI.loc()
spoofed = spoof.LockTo()
fbihost = Antena.send.request(spoofed).find.host.computer.data(host)
ip, query = js.search{"What is my ip"}
deuth = win.create.packet.type.deauth{host=fbihost, direct=ip}
win.arp.spoof(antena.clients.waiting(permission = True{responses = sys.AI.exec(Data.SearchFor *.sendto = ip)}))

