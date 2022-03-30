
def sjf(processes):
    readyQ = []
    global te
    te = 0
    completeQ = []

    def complete(pro, processes):
        global te
        completeQ.append(pro)
        te += pro.burstTime
        rmov = []
        for pro in processes:
            if pro.arrivalTime <= te:
                readyQ.append(pro)
                rmov.append(pro)
        for pro in rmov:
            processes.remove(pro)
    processes.sort(key=lambda pro: pro.arrivalTime)
    readyQ.append(processes.pop(0))
    complete(readyQ.pop(0), processes)
    while len(readyQ):
        readyQ.sort(key=lambda pro: pro.burstTime)
        complete(readyQ.pop(0), processes)
    for pro in completeQ:
        if completeQ.index(pro) == 0:
            pro.completionTime = pro.arrivalTime + pro.burstTime
            ct = pro.arrivalTime + pro.burstTime
        else:
            pro.completionTime = ct + pro.burstTime
            ct = pro.burstTime + ct

    return(completeQ)


def sjfP(processes):
    readyQ = []
    completeQ = []
    global te
    te = 0

    def complete(pro, processes):
        global te
        te += 1
        pro.remainingBurstTime -= 1
        completeQ.append(pro)
        rmov = []
        if len(processes) > 0:
            for i in processes:
                if i.arrivalTime <= te:
                    readyQ.append(i)
                    rmov.append(i)
            if len(rmov):
                for i in rmov:
                    processes.remove(i)
        if pro.remainingBurstTime > 0:
            readyQ.append(pro)
        else:
            pro.completionTime = te
# When two process have same arrival time it will sort according to burst time
    processes.sort(key=lambda pro: (pro.arrivalTime, pro.burstTime))
    readyQ.append(processes.pop(0))
    # complete(processes.pop(0), processes)
    complete(readyQ.pop(0), processes)
    while len(readyQ) > 0:
        readyQ.reverse()
        readyQ.sort(key=lambda pro: pro.remainingBurstTime)
        complete(readyQ.pop(0), processes)
    # queue = list(set(completeQ))
    return completeQ
