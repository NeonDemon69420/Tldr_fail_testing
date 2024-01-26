from utils.ipAddresses import getIPAddresses
from utils.multiprocess import startMultiProcess, workerCheckIfPortIsOpen

ipAddresses = getIPAddresses()
numOfIPAddresses = len(ipAddresses)

print(f"Number of ip addresses to check: {numOfIPAddresses}")

listOfWebsites = startMultiProcess(64, workerCheckIfPortIsOpen, *ipAddresses)

print(f"Number of websites: {len(listOfWebsites)}")

