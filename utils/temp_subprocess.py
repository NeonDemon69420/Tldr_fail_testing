import subprocess

file = open("sample.txt", "w")
file.write("")
file.close()


def checkIfvalid(IP):
    result = subprocess.run(
        ["nmap", "--script", "./scan-web.nse", IP], stdout=subprocess.PIPE, text=True)

    if "open443" in result.stdout:
        filehandle = open("sample.txt", "a")
        filehandle.writelines(IP + "\n")
        filehandle.close()
        return True
    else:
        return False


print(checkIfvalid("cyberstorm.mu"))
print(checkIfvalid("itbox.mu"))
print(checkIfvalid("8.8.8.8"))
print(checkIfvalid("172.56.89.45"))
print(checkIfvalid("55.168.25.79"))
