import multiprocessing
import subprocess

def worker_get_valid_ip_addresses(process_num, manager, number_of_processes, return_dictionary, *args):
    list_length = int(len(args[0])/number_of_processes)
    list = args[0][list_length*process_num:list_length*(process_num+1)]

    for ip_address in list:
        print(f"Checking ip address {ip_address} if port 443 is open.")

        if get_valid_ip_addresses(ip_address):
            append_to_array(manager, str(process_num), ip_address, return_dictionary)

# number_of_processes must be a power of 2 (i.e., 2, 4, 8, 16, ...)
def start_multiprocessing(number_of_processes, worker, *args):
    manager = multiprocessing.Manager()
    return_dictionary = manager.dict()
    jobs = []
    for i in range(number_of_processes):
        process = multiprocessing.Process(target=worker, args=(
            i, manager, number_of_processes, return_dictionary, args))
        jobs.append(process)
        process.start()

    for proc in jobs:
        proc.join()

    flattened_list = [item for sublist in return_dictionary.values() for item in sublist]
    return flattened_list


def append_to_array(manager, key, value, dict):
    if key not in dict:
        dict[key] = manager.list()
    dict[key].append(value)


def get_valid_ip_addresses(ip):
    result = subprocess.run(["nmap", "--script", "./utils/scan-web.nse", ip], stdout=subprocess.PIPE, text=True)
    extracted_result = [line for line in result.stdout.splitlines() if line.startswith("open")]
    if len(extracted_result) > 0:
        if "open-443" in extracted_result:
            print(f"Port 80 and 443 is open for ip address {ip}")
            file = open("./results/ip_addresses_with_port80and443_open.txt", "a")
            file.writelines(ip + "\n")
            file.close()
            return True
        else:
            print(f"Only port 80 is open for ip address {ip}")
            file = open("./results/ip_addresses_with_port80_open.txt", "a")
            file.writelines(ip + "\n")
            file.close()
            return False
    else:
        print(f"Port 80 and 443 is not open for ip address {ip}")
        return False