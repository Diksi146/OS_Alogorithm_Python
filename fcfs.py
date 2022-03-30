def fcfs(processes):
    readyQ = []
    completeQ = []
    ct = 0
    processes.sort(key=lambda x: x.arrivalTime)
    for pro in processes:
        completeQ.append(pro)
    for pro in processes:
        if processes.index(pro) == 0:
            pro.completionTime = pro.arrivalTime + pro.burstTime
            ct = pro.arrivalTime + pro.burstTime
        else:
            pro.completionTime = ct + pro.burstTime
            ct = pro.burstTime + ct
    return(completeQ)
