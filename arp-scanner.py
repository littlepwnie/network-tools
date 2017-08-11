import sys
from datetime import datetime
from scapy.all import srp,Ether,ARP,conf

try:
    interface = raw_input("[*] Enter desired interface: ")
    ips = raw_input("[*] Enter IP range to scan: ")

except Keyboardinterrupt:
    print "\n[*] User forced shutdown"
    print "\n[*] Terminating..."
    sys.exit(1)

print "\n[*] Scanning..."
start_time=datetime.now()

conf.verb = 0
ans, uans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips), timeout = 2, iface = interface, inter = 0.1)

print "MAC - IP\n"
for snd,rcv in ans:
    print rcv.sprintf(r"%Ether.src% - %ARP.psrc%")
stop_time = datetime.now()
total_time = stop_time - start_time
print ("\n[*] Scan completed in: %s" %(total_time))
