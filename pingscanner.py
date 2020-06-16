# made for python 3.x (tested 3.6.9)
import subprocess
import os

print("Pinger for /24")
with open(os.devnull, "wb") as limbo:
        for n in range(1, 254):
                ip="192.168.30.{0}".format(n)
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                        stdout=limbo, stderr=limbo).wait()
                if not result:
                        print(ip, "active")
