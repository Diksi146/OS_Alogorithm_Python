from tabulate import tabulate


def calCompletionTime(queue):
    for pro in queue:
        if queue.index(pro) == 0:
            ct = pro[2]
            pro.append(ct)
        else:
            ct = ct + pro[2]
            pro.append(ct)


def calWaitingTime(queue):
    for pro in queue:
        wt = pro[4] - pro[2]
        pro.append(wt)


def calTurnaroundTime(queue):
    for pro in queue:
        tat = pro[3] - pro[1]
        pro.append(tat)


def calAverage(queue):
    totalWt = totalTat = totalCt = 0
    for pro in queue:
        totalCt += pro[3]
        totalTat += pro[4]
        totalWt += pro[5]
    averageCt = totalCt / (len(queue)+1)
    averageTat = totalTat / (len(queue)+1)
    averageWt = totalWt / (len(queue)+1)
    print()
    print(f"Average Completion Time of Processes is {round(averageCt,3)}")
    print(f"Average Turn Around Time of Processes is {round(averageTat,3)}")
    print(f"Average Waiting Time of Processes is {round(averageWt,3)}")


def printData(queue):
    head = ["Process ID", "Arrival time", "Burst time",
            "Completion Time", "Turn Around Time", "Waiting Time"]
    print(tabulate(queue, headers=head, tablefmt="grid"))


def main():
    l = [
        # ["p1", "arrival time","burst time", "completion Time", "Turn Around Time", "Waiting Time"]
        ["p1", 2, 6],
        ["p2", 5, 2],
        ["p3", 1, 8],
        ["p4", 0, 3],
        ["p5", 4, 4]
    ]
    print("\n------- Input Process Data ------- \n")
    print(tabulate(l, headers=["Process ID",
          "Arrival time", "Burst time"], tablefmt="grid"))
    sortedList = sorted(l, key=lambda x: x[1], reverse=False)
    readyQ = []
    completeQ = []
    completeQ.append(sortedList.pop(0))
    executionTime = completeQ[0][2]
    length = len(sortedList)
    while length != 0:
        for pro in sortedList:
            if pro[1] <= executionTime:
                readyQ.append(pro)
        readyQ.sort(key=lambda x: x[2], reverse=False)
        if readyQ:
            r = readyQ.pop(0)
            completeQ.append(r)
            sortedList.remove(r)
            readyQ.clear()
            executionTime = executionTime + completeQ[len(completeQ) - 1][2]
        else:
            break
        length = length - 1

    calCompletionTime(completeQ)
    calTurnaroundTime(completeQ)
    calWaitingTime(completeQ)
    print("\n------- SJF Non preamptive ------- \n")
    printData(completeQ)
    calAverage(completeQ)


main()
