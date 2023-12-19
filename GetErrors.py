import subprocess



with open ("FailedInfo.txt", "w") as outputfile:
    process = subprocess.Popen(["python3", "failed_tldr_errors.py"],stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    output, _ = process.communicate()

    outputfile.write(output)

outputfile.close()
