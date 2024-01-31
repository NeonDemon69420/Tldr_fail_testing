from utils.ip_addresses import get_ip_addresses
from utils.multiprocessing import start_multiprocessing, worker_get_valid_ip_addresses, default_multiprocessing_return_function

ip_addresses = get_ip_addresses()
num_of_ip_addresses = len(ip_addresses)

print(f"Number of ip addresses to check: {num_of_ip_addresses}")

list_of_websites = start_multiprocessing(64, worker_get_valid_ip_addresses, default_multiprocessing_return_function, *ip_addresses)

print(f"Number of websites: {len(list_of_websites)}")

