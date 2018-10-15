#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input
remoteServer = raw_input("Enter a remote host to scan: ")
m = int(1)
n = int(1025)
option = raw_input("Default port options: y/n ")

if (option == "n"):
    n = int(raw_input("Enter a starting port (can't be smaller than 1): "))
    m = int(raw_input("Enter ending port (cant be greater than 65535): "))

remoteServerIP  = socket.gethostbyname(remoteServer)

print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60

t1 = datetime.now()

try:
    for port in range(m,n):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: 	Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

t2 = datetime.now()

total = t2 - t1

print 'Scanning Completed in: ', total
