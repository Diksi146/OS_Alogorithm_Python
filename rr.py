def roundRobin(processes):
    readyQ = []
    completeQ = []
    global totalExecutionTime
    timeQuantum = int(
        input("What is a Time Quantum for round robin algorithm :- "))
    totalExecutionTime = 0

    def complete(pro):
        global totalExecutionTime
        if pro.remainingBurstTime <= timeQuantum:
            totalExecutionTime += pro.remainingBurstTime
            pro.remainingBurstTime = 0
        else:
            pro.remainingBurstTime -= timeQuantum
            totalExecutionTime += timeQuantum
        completeQ.append(pro)
        # Adding Processes to the ready queue
        if len(processes) > 0:  # check if processes queue is empty
            rmov = []
            for i in processes:
                if i.arrivalTime <= totalExecutionTime:
                    readyQ.append(i)
                    rmov.append(i)
            for i in rmov:
                processes.remove(i)
        if pro.remainingBurstTime > 0:
            readyQ.append(pro)
        else:
            pro.completionTime = totalExecutionTime

    # Code for fist process to execute
    processes.sort(key=lambda x: x.arrivalTime)
    readyQ.append(processes.pop(0))
    complete(readyQ.pop(0))
    while len(readyQ) > 0:
        complete(readyQ.pop(0))

    # completedQ = list(set(completeQ))
    return completeQ
