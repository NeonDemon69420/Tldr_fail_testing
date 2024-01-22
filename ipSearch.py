from utils.ipAddresses import getIPAddresses
from utils.port import isPortOpen


ipAddresses = getIPAddresses()

numOfIPAddresses = len(ipAddresses)
listOfWebsites = []
    
print(f"Number of ip addresses to check: {numOfIPAddresses}")
count = 0
skippedIP = 0
for ipAddress in ipAddresses:
    print(f"Checking ip address {ipAddress} if port 443 is open. {count}/{numOfIPAddresses}")
    count += 1
    if isPortOpen(ipAddress, 443):
        listOfWebsites.append(ipAddress)
    else:
        skippedIP += 1
        print(f"Skipped ip address {ipAddress} because port 443 is not open. {skippedIP} ip addresses skipped so far.")

numOfWebsites = len(listOfWebsites)
print(f"Number of websites: {numOfWebsites}")

