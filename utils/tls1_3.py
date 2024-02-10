import subprocess
import re
import sys

from sympy import true

CIPHERS = 'ALL:eNULL'
ciphers = [cipher.replace("\n", "") for cipher in subprocess.check_output(['openssl', 'ciphers', '-tls1_3', '-s', CIPHERS]).decode().split(':')]
list_ip=open("results/vulnerability_result/non_vulnerable_ip_addresses.txt","r")
result=""
for counter in list_ip:
    flag =False
    for cipher in ciphers:
        try:
            completed_process = subprocess.run(['openssl', 's_client', '-tls1_3', '-ciphersuites', cipher, '-connect', f'{counter}:443'], input=b'', stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output = completed_process.stdout.decode()
            
            if re.search(f'Cipher is {cipher}|Cipher    :', output):
                result = 'YES'
                flag =True
                f=open("HasTLS1_3.txt","a")#rename tls 1.3
                f.write(counter)
                f.close()
                break
        except subprocess.TimeoutExpired:
            pass

    if flag==False:
        f=open("DoesNotHaveTLS1_3.txt","a")#tls <1.3(version)
        f.write(counter)
        f.close()
