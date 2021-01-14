#!/bin/bash
cyan='\e[0;36m'
green='\e[0;32m'
lightgreen='\e[1;32m'
white='\e[1;37m'
RED='\033[0;31m'
yellow='\e[1;33m'
NC='\033[0m'
blue='\e[1;34m'
path=`pwd` 
echo -e $RED"
..######..##....##.########..########.########...######..########.....###.....######..##....##
.##....##..##..##..##.....##.##.......##.....##.##....##.##.....##...##.##...##....##.##...##.
.##.........####...##.....##.##.......##.....##.##.......##.....##..##...##..##.......##..##..
.##..........##....########..######...########..##.......########..##.....##.##.......#####...
.##..........##....##.....##.##.......##...##...##.......##...##...#########.##.......##..##..
.##....##....##....##.....##.##.......##....##..##....##.##....##..##.....##.##....##.##...##.
..######.....##....########..########.##.....##..######..##.....##.##.....##..######..##....##
"
echo -e $blue"[+] Installing dependencies...."
pip install python-geoip
pip install python-geoip-geolite2
pip install python-geoip-python3
pip install colorama
pip install subprocess.run
pip install ipwhois
pip install wheel
sudo mkdir /usr/share/cybercrack-framework
echo "[+] Created a new directory named cybercrack-framework"
mv -v $path"Cybercrack/* /usr/share/cybercrack-framework"
echo "[+] Started to edit your bashrc"
echo "[+] Type your sudo password bellow"
sudo echo "export PATH=$PATH:/usr/share/cybercrack-framework/CyberCrack.py" >> ~/.bashrc	
echo "[+] Done editing the bashrc"
echo "[+] Finalizing.."
echo -e $blue"
First type source ~/.bashrc and
Now go and type CyberCrack.py
"