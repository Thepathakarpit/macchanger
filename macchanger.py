#i/usr/bin/env python

#x: device
#y: mac address

import subprocess
import optparse
import re

def parsing():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--i", dest="interface", help= "Interface whose MAC address you want to change.")
    parser.add_option("-m", "--mac", dest="mac", help= "MAC address you want to change to.")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please enter the interface or for more info use --help.")
    if not options.mac:
        parser.error("Please enter the new MAC or for more info use --help.")
    return options

def mac_changer(x,y):
    print("Mac address changer activated.\n")
    subprocess.call(["sudo", "ifconfig", x, "down"])
    subprocess.call(["sudo", "ifconfig", x, "hw", "ether", y])
    subprocess.call(["sudo", "ifconfig", x, "up"])

def check(x):
    macrn = subprocess.check_output(["ifconfig", x])
    
    oldmac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(macrn))

    if oldmac:
    
        if oldmac.group(0) == str(options.mac):
            print("Mac address has been successfully changed from " "to " + options.mac)
        else:
            print("Mac cannot be changed to mentioned mac address.")
    else:
        print("Cannot read mac address")

    
options = parsing()
mac_changer(options.interface, options.mac)
check(options.interface)


#Fin at 10:01PM on 26th of july 2022 in Mandla @ my home
