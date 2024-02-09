import subprocess
from utils.multiprocessing import start_multiprocessing, worker_check_tls_enabled, empty

with open("./results/firewall_result/ip_addresses_with_no_firewall.txt", "r") as file:
    ip_addresses = [line.replace("\n", "") for line in file.readlines()]

start_multiprocessing(1, worker_check_tls_enabled, empty, *ip_addresses)