import requests
 

for addr in ['99:99:99:99:99:99']:
    vendor = requests.get('http://api.macvendors.com/' + addr).text

print(addr, vendor)