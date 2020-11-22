#sudo nmap -n -sn 192.168.1.0/24 | awk '/Nmap scan report for/{printf $5;}/MAC Address:/{print " => "substr($0, index($0,$3)) }' | sort

#SCAN ALL PORTS OS ALL ALIVE HOSTS
#sudo nmap -sU 192.168.100.1/24 

#ifconfig | grep "inet " | grep -Fv 127.0.0.1 | awk '{print$2}'

#P2 = pip install python-nmap / P3 = pip3 install python-nmap
import nmap
import os
from datetime import datetime

# Examples in nmap.orOg:
# REF:https://nmap.org/book/osdetect.html

class Network(object):
    def __init__(self):
        self.ip = str(os.popen('arp -a | grep gateway | cut -d "(" -f2 | cut -d ")" -f1 | awk \'{print $1"/24"}\'').read()) #get gateway ip
        #print(self.ip)
        
    def networkscan(self):
        #network = self.ip + '/24' #gateway/mask

        print("--[SCANNING]--")

        nm = nmap.PortScanner()
        #nm.scan(hosts='192.168.1.0/24', arguments='-n -sn -PE -PA21,23,80,3389') 
        nm.scan(hosts=self.ip, arguments='-sS')
        for n in nm.all_hosts():
            print(nm[n])
            #print(nm[n]['addresses']['ipv4'])       #IP
            #print(nm[n]['addresses']['mac'])       #MAC
            #self.mac = str(os.popen('').read())    #MAC
            #print(nm[n]['vendor'])                  #FABRICANTE/MAC
            #print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) #DISCOVER TIME
            print("*"*30)

        #hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

if __name__ == "__main__":

    n = Network()
    n.networkscan()  

    