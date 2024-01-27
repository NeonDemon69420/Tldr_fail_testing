import multiprocessing
from utils.port import isPortOpen

def workerCheckIfPortIsOpen(processNum, manager, numberOfProcesses, returnDictionary, *args):
    listLength = int(len(args[0])/numberOfProcesses)
    list = args[0][listLength*processNum:listLength*(processNum+1)]
    for ipAddress in list:
        print(f"Checking ip address {ipAddress} if port 443 is open.")
        if isPortOpen(ipAddress, 443):
            print(f"Port 443 is open for ip address {ipAddress}")
            appendToArray(manager, str(processNum), ipAddress, returnDictionary)
        else:
            print(f"Port 443 is not open for ip address {ipAddress}")

# numberOfProcesses must be a power of 2 (i.e., 2, 4, 8, 16, ...)
def startMultiProcess(numberOfProcesses, worker, *args):
    manager = multiprocessing.Manager()
    returnDictionary = manager.dict()
    jobs = []
    for i in range(numberOfProcesses):
        process = multiprocessing.Process(target=worker, args=(i, manager, numberOfProcesses, returnDictionary, args))
        jobs.append(process)
        process.start()

    for proc in jobs:
        proc.join()

    flattenedList = [item for sublist in returnDictionary.values() for item in sublist]
    return flattenedList

def appendToArray(manager, key, value, dict):
    if key not in dict:
        dict[key] = manager.list()
    dict[key].append(value)





