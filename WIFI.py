#Part 1: Connect to Internet

from network import WLAN, STA_IF
from network import mDNS
import time

wlan = WLAN(STA_IF)
wlan.active(True)

wlan.connect('<add here>', '<add here>', 5000)

for x in range(0,10):
    if not wlan.isconnected():
        print("Waiting for wlan connection")
        time.sleep(1)
    else:
        break
print("Wifi connected at", wlan.ifconfig()[0])

#Advertise as 'hostname', alternative to IP address
try:
    hostname = 'wifinetwork'
    mdns = mDNS(wlan)
    mdns.start(hostname, "MicroPython REPL")
    mdns.addService('_repl', '_tcp', 23, hostname)
    print("Advertised locally as {}.local".format(hostname))
except OSERROR:
    print("Failed starting mDNS server - already started?")

#start telnet server for remote login
from network import telnet

print("start telnet server")
telnet.start(user='user name ...', password='telnet password ...')

# fetch NTP time
from machine import RTC

print("inquire RTC time")
rtc = RTC()
rtc.ntp_sync(server="pool.ntp.org")

timeout = 10
for _ in range(timeout):
    if rtc.synced():
        break
    print("Waiting for rtc time")
    time.sleep(1)

if rtc.synced():
    print(time.strftime("%c", time.localtime()))
else:
    print("could not get NTP time")
