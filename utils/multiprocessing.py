import multiprocessing
import subprocess

def worker_get_valid_ip_addresses(process_num, manager, number_of_processes, return_dictionary, *args):
    list_length = int(len(args[0])/number_of_processes)
    list = args[0][list_length*process_num:list_length*(process_num+1)]

    for ip_address in list:
        print(f"Checking ip address {ip_address} if port 443 is open.")
        if get_valid_ip_addresses(ip_address):
            append_to_array(manager, str(process_num), ip_address, return_dictionary)


def worker_check_ip_addresses_tldr(process_num, manager, number_of_processes, return_dictionary, *args):
    list_length = int(len(args[0])/number_of_processes)
    list = args[0][list_length*process_num:list_length*(process_num+1)]

    for i, ip_address in enumerate(list):
        print(f"Process {process_num} is {(i/len(list))*100:.2f}% done.")
        try:
            result = subprocess.run(["python3", "./tldr_fail_test.py", ip_address], stdout=subprocess.PIPE, text=True, timeout=10)

            if not "[WinError 10054]" in result.stdout:
                append_to_array(manager, str(process_num), (ip_address, False), return_dictionary)
            else:
                append_to_array(manager, str(process_num), (ip_address, True), return_dictionary)
        except subprocess.TimeoutExpired:
            append_to_array(manager, str(process_num), (ip_address, True), return_dictionary)

def worker_classify_ip_addresses(process_num, manager, number_of_processes, return_dictionary, *args):
    list_length = int(len(args[0])/number_of_processes)
    list = args[0][list_length*process_num:list_length*(process_num+1)]
    
    for i, ip_address in enumerate(list):
        print(f"Process {process_num} is {(i/len(list))*100:.2f}% done.")
        try:
            result = subprocess.run(["nmap", ip_address.strip(), "--script", "whois-ip.nse", "-Pn"], stdout=subprocess.PIPE, text=True)
            netname = extract_netname(result.stdout)
            if netname == "":
                append_to_array(manager, "Unknown", ip_address, return_dictionary)
            else:
                append_to_array(manager, netname, ip_address, return_dictionary)
        except subprocess.TimeoutExpired:
            append_to_array(manager, "Unknown", ip_address, return_dictionary)

def worker_check_if_tls_enabled(process_num, manager, number_of_processes, return_dictionary, *args):
    list_length = int(len(args[0])/number_of_processes)
    list = args[0][list_length*process_num:list_length*(process_num+1)]

    for i, ip_address in enumerate(list):
        try:
            result = subprocess.run(["nmap", "--script", "./utils/test_tls.nse", "-p", "443", ip_address, "-Pn"], stdout=subprocess.PIPE, text=True, timeout=120)
            print(result.stdout)
            if "No supported ciphers found" in result.stdout:
                file = open("./results/tls_result/ip_addresses_with_no_tls_enabled.txt", "a")
                file.writelines(ip_address + "\n")
                file.close()
            else:
                file = open("./results/tls_result/ip_addresses_with_tls_enabled.txt", "a")
                file.writelines(ip_address + "\n")
                file.close()
        except subprocess.TimeoutExpired:
            file = open("./results/tls_result/ip_addresses_with_no_tls_enabled.txt", "a")
            file.writelines(ip_address + "\n")
            file.close()
        print(f"Process {process_num} is {((i+1)/len(list))*100:.2f}% done.")



def start_multiprocessing(number_of_processes, worker, multiprocessing_return_function, *args):
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

    return multiprocessing_return_function(return_dictionary)

def default_multiprocessing_return_function(return_dictionary):
    return [item for sublist in return_dictionary.values() for item in sublist]

def classify_ip_addresses_return_function(return_dictionary):
    return return_dictionary


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
            file = open("./results/ip_addresses_with_port_open/ip_addresses_with_port80and443_open.csv", "a")
            file.writelines(ip + "\n")
            file.close()
            return True
        else:
            return False
    else:
        print(f"Port 80 and 443 is not open for ip address {ip}")
        return False
    
def extract_netname(result):
    netname_index = result.find('netname')
    netname_end_index = result.find('\n', netname_index)
    netname_line = result[netname_index:netname_end_index]
    netname_parts = netname_line.split(':')
    return netname_parts[-1].strip()

def empty(arg):
    return arg