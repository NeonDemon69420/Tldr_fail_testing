from utils.multiprocessing import start_multiprocessing, worker_check_if_behind_firewall, empty

with open('results/ip_addresses_with_port_open/ip_addresses_with_port80and443_open.csv', 'r') as file:
    ip_addresses = [line.replace('\n', '') for line in file.read().splitlines()]

start_multiprocessing(129, worker_check_if_behind_firewall, empty, *ip_addresses)

