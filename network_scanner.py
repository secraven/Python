#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    #print(answered_list[0])

    print("IP\t\t\tMAC Address\n-----------------------------------------")

    for element in answered_list:
       #print(element[1].show())
       print(element[1].psrc + "\t\t" + element[1].hwsrc)
       #print(element[1].hwsrc)
       #print("-----------------------------------------")

    #print(answered_list.summary())


    #arp_request.show()
    #broadcast.show()
    #print(arp_request_broadcast.summary())
    #arp_request_broadcast.show()
    #print(broadcast.summary())
    #scapy.ls(scapy.Ether())
    #arp_request.pdst = ip
    #print(arp_request.summary())
    #scapy.ls(scapy.ARP())


#scan("10.0.2.15")
scan("10.0.2.1/24")


