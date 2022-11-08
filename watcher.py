import time as t 
import os
import sys
import urllib.requests


#Delay
delay = 1

#Start of the script.
def start(host):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

#Start of the scanner.
def scanner(host):
    try:
        target = socket.gethostbyname(host)
        # will scan ports between 1 to 65,535
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            
            # returns an error indicator
            result = s.connect_ex((target,port))
            if result ==0:
                print(f"Port {port} is open")
            s.close()

#Grabs the pubkey of the website if there is.
def grabber(host):
    try:
        response = request.urlretrieve("https://www.facebook.com/favicon.ico", "facebook.ico")
        return True
    except:
        return False


host = input("Enter target: ")
if start():
    print(f"Gathering info from {host}")
else:
    print(f"Connection error from {host}")
    sys.exit()

if scanner():
    print(f"Scanning connected target {host} !")
else:
    print("Failed to scan -skipping-")

