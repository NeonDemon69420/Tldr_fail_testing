import pandas as pd

def extract_ip_addresses():
    range_of_ip_addresses = pd.read_excel(io='files/range_of_ip_addresses.xlsx', sheet_name='ip_addresses')
    return range_of_ip_addresses[['start_ip', 'count']].values.tolist()

def get_ip_addresses():
    list = extract_ip_addresses()

    range_of_ip_addresses_with_count = list[3:4]
    ip_addresses = []
    
    for i in range(len(range_of_ip_addresses_with_count)):
        for j in range(range_of_ip_addresses_with_count[i][1]):
            ip_addresses.append(increment_ip(range_of_ip_addresses_with_count[i][0], j))
                    
    return ip_addresses


def increment_ip(ip, n):
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


list = extract_ip_addresses()

for item in list:
    print(item)