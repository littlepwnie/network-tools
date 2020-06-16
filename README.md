# Network Tools
A personal collection of simple and effective network tools

## Port Scanner
Lists the available ports of a specific remote host.

Input the remote host to scan and opt to scan for specific ports.

To exectute:
```
python port-scanner.py
```

## ARP scanner
The Address Resolution Protocol (ARP) uses a simple message format containing one address resolution request or response. It displays every active `IPv4` Devices connected on the network.

To execute:
```
python arp-scanner.py
```

## Ping scanner
A simple script that discovers active hosts. It displays every pingable `IPv4` Devices connected on a /24 network.

Change in the script the subnet and optionally the range if you don't want the whole /24.

To execute:
```
python pingscanner.py
```
