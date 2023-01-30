import subprocess

blacklist = ['insert SSIDs here'] #you can also just put one wifi SSID
vpn_config = "insert config name here" #put here the name of the Wireguard Profile


command = ['C:\\Program Files\\WireGuard\\wireguard.exe',
           '/installtunnelservice',
           f'C:\\Program Files\\WireGuard\\Data\\Configurations\\{vpn_config}.conf.dpapi']

#This part will querry the current SSID from the netsh tool and parse it to
#extract only the SSID
interface = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'])
interface_lines = interface.splitlines()
SSID = (interface_lines[8].decode('utf-8')).split(": ")[1]

#if the parsed SSID is not in the blacklist we run the activation command
if SSID not in blacklist:
    print("SSID not in blacklist, starting VPN...")
    subprocess.run(command)
elif:
    print("SSID is in blacklist, maybe next time...")
