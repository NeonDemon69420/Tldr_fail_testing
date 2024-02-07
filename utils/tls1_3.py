import subprocess
import re
import sys

CIPHERS = 'ALL:eNULL'
host = sys.argv[1]
ciphers = [cipher.replace("\n", "") for cipher in subprocess.check_output(['openssl', 'ciphers', '-tls1_3', '-s', CIPHERS]).decode().split(':')]

for cipher in ciphers:
    try:
        completed_process = subprocess.run(['openssl', 's_client', '-tls1_3', '-ciphersuites', cipher, '-connect', f'{host}:443'], input=b'', stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = completed_process.stdout.decode()
        if ':error:' in output:
            result = 'NO'
        elif re.search(f'Cipher is {cipher}|Cipher    :', output):
            result = 'YES'
        else:
            result = 'NO'
    except subprocess.TimeoutExpired:
        result = 'NO'

    print(f'{cipher}:{result}')