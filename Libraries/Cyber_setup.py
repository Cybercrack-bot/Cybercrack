def update():
    update_complete = False
    import subprocess
    import platform
    input("Hit enter to continue >> ")
    if platform.system() == 'Windows':
        subprocess.call("git pull https://github.com/Cybercrack-bot/Cybercrack.git", shell=True)
        subprocess.call("cd ..", shell=True)
        subprocess.call("Install.bat", shell=True)
    elif platform.system() == 'Linux':
        subprocess.call("git pull https://github.com/Cybercrack-bot/Cybercrack.git", shell=True)
        subprocess.call("cd ..", shell=True)
        subprocess.call("Install.sh", shell=True)
    else:
        subprocess.call("git pull https://github.com/Cybercrack-bot/Cybercrack.git", shell=True)
        subprocess.call("cd ..", shell=True)
        print("[+] Run the install.sh")
    update_complete = True
    input("Hit enter to finish >> ")