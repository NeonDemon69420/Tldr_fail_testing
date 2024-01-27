import pandas as pd

def extractIPAddresses():
    rangeOfIPAddresses = pd.read_excel(io='files/rangeOfIPAddresses.xlsx', sheet_name='ipAddresses')
    return rangeOfIPAddresses[['StartIP', 'Count']].values.tolist()

def getIPAddresses():
    list = extractIPAddresses()

    rangeOfIPAddressesWithCount = list[3:4]
    ipAddresses = []
    
    for i in range(len(rangeOfIPAddressesWithCount)):
        for j in range(rangeOfIPAddressesWithCount[i][1]):
            ipAddresses.append(incrementIP(rangeOfIPAddressesWithCount[i][0], j))
                    
    return ipAddresses


def incrementIP(ip, n):
    num = ip_to_number(ip)
    num += n
    return number_to_ip(num)

def ip_to_number(ip):
    parts = [int(part) for part in ip.split(".")]
    num = 0

    for part in parts:
        num = num * 256 + part

    return num


def number_to_ip(num):
    parts = []
    for _ in range(4):
        parts.insert(0, str(num & 0xFF))
        num >>= 8

    return ".".join(parts)


list = extractIPAddresses()

for item in list:
    print(item)