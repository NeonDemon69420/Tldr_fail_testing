from utils.multiprocessing import start_multiprocessing, worker_classify_ip_addresses, classify_ip_addresses_return_function

with open('./results/vulnerability_result/vulnerable_ip_addresses.txt', 'r') as file:
    ip_addresses = [line.replace("\n", "") for line in file.readlines()]

dict_classified_ip_addresses = start_multiprocessing(121, worker_classify_ip_addresses, classify_ip_addresses_return_function, *ip_addresses)


with open("./results/classified_by_provider/classified_ip_addresses_overview.txt", "w") as file:
    for key in dict_classified_ip_addresses:
        size_of_classified_ip_addresses = len(dict_classified_ip_addresses[key])
        size_of_all_ip_addresses = len(ip_addresses)
        percentage = (size_of_classified_ip_addresses/size_of_all_ip_addresses)*100
        file.write(f"{key}: {size_of_classified_ip_addresses} ({percentage:.2f}%)\n")


with open("./results/classified_by_provider/classified_ip_addresses.txt", "w") as file:
    for key, value in dict_classified_ip_addresses.items():
        file.write(f"{key}: {value}\n")