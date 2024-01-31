import multiprocessing
from multiprocessing import process
import subprocess

site_array = []
# Change files for each batch
file = open(r"files\IP_Batch2.txt")
for site in file:
    site_array.append(site.replace("\n", ""))
file.close()


def Process(array, Result_queue):
    for item in array:
        try:
            item = item.replace("\n", "")
            result = subprocess.run(
                ["python3", "./tldr_fail_test.py", item], stdout=subprocess.PIPE, text=True, timeout=15)

            if not "[WinError 10054]" in result.stdout:
                print("success")
                filehandle = open("CorrectIP_Batch2.txt", "a")

                filehandle.write(item + "\n")
                filehandle.close()
            else:
                print("failure")
                fileError = open("failedIP_Batch2.txt", "a")
                fileError.write(item + "\n")
                fileError.close()


        except subprocess.TimeoutExpired:
            print("Subprocess timeout")
           
            fileError = open("failedIP_Batch2.txt", "a")
            fileError.write(item + "\n")
            fileError.close()

        except Exception as e:
            print(e)
            
            fileError = open("failedIP_Batch2.txt", "a")
            fileError.write(item + "\n")
            fileError.close()

    Result_queue.put = 1


if __name__ == "__main__":
    resultQueue = multiprocessing.Queue()

    processes = []
    numofprocesses = 103
    chunckSize = len(site_array)//numofprocesses

    chunks = [site_array[i:i+chunckSize]
              for i in range(0, len(site_array), chunckSize)]

    for pieces in chunks:
        process = multiprocessing.Process(
            target=Process, args=(pieces, resultQueue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results = []

    while not resultQueue.empty():
        results.append(resultQueue.get())

    print(results)