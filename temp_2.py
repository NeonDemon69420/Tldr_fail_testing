from utils.multiprocessing import start_multiprocessing, worker_check_ip_addresses_tldr, default_multiprocessing_return_function

with open('results/tls_result/IP_batch2.txt', 'r') as file:
    ip_addresses = [line.replace("\n", "") for line in file.readlines()]
file.close()

ip_addresses = start_multiprocessing(199, worker_check_ip_addresses_tldr, default_multiprocessing_return_function, *ip_addresses)

vulnerable_ip_addresses = [ip_address for ip_address, failed in ip_addresses if failed]
non_vulnerable_ip_addresses = [ip_address for ip_address, failed in ip_addresses if not failed]

with open("./results/vulnerability_result/vulnerability_result_copy_2.txt", "w") as file:
    file.write(f"Total number of ip addresses: {len(ip_addresses)}\n")
    file.write(f"Number of vulnerable ip addresses: {len(vulnerable_ip_addresses)}\n")
    file.write(f"Number of non vulnerable ip addresses: {len(non_vulnerable_ip_addresses)}\n")
    file.write(f"Percentage of vulnerable ip addresses: {(len(vulnerable_ip_addresses)/len(ip_addresses))*100}%\n")

with open("./results/vulnerability_result/vulnerable_ip_addresses_copy_2.txt", "w") as file:
    file.writelines(ip + "\n" for ip in vulnerable_ip_addresses)

with open("./results/vulnerability_result/non_vulnerable_ip_addresses_copy_2.txt", "w") as file:
    file.writelines(ip + "\n" for ip in non_vulnerable_ip_addresses)