import subprocess

def CheckTLS(ipAddress):
    result = subprocess.run(["nmap", "--script", "ssl-enum-ciphers.nse", "-p", "443", ipAddress], stdout=subprocess.PIPE, text=True, timeout=15)

    if "TLSv1.3" in result.stdout:
        return True
    else:
        return False