# Process Class
from tabulate import tabulate


class process:
    processes = []

    def __init__(self, processID, arrivalTime, burstTime):
        self.processID = "P" + str(processID)
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.completionTime = 0
        self.turnAroundTime = 0
        self.waitingTime = 0
        self.remainingBurstTime = burstTime

    def calTurnaroundTime(self):
        self.turnAroundTime = self.completionTime - self.arrivalTime

    def calWaitingTime(self):
        self.waitingTime = self.turnAroundTime - self.burstTime


def createProcess():
    processes = []
    p = input("Number of processes :- ")
    for i in range(int(p)):
        x, y = input(
            f"Enter the arrival time and burst time for {i+1}st process :- ").split()
        processes.append(process(i+1, int(x), int(y)))
    return processes


def printQ(q):
    for i in q:
        print(f"{i.processID} {i.arrivalTime} {i.burstTime} {i.remainingBurstTime}")


def printData(queue, completionQ):
    avgW = 0
    avgC = 0
    avgT = 0
    head = [
        "Process ID", "Arrival time", "Burst time",
        "Completion Time", "Turn Around Time", "Waiting Time"]
    n = len(queue)
    # data = [[], [], []]
    data = []

    # for i in range(len(queue)):
    #     print(i)
    for i in range(len(queue)):
        j = []
        j.append(queue[i].processID)
        j.append(queue[i].arrivalTime)
        j.append(queue[i].burstTime)
        j.append(queue[i].completionTime)
        j.append(queue[i].turnAroundTime)
        j.append(queue[i].waitingTime)
        data.append(j)

    print(tabulate(data, headers=head, tablefmt="grid"))
    for i in queue:
        avgC += i.completionTime
        avgT += i.turnAroundTime
        avgW += i.waitingTime
    avgC /= len(queue)
    avgT /= len(queue)
    avgW /= len(queue)
    print("Completion Queue Is")
    for i in completionQ:
        print(f"{i.processID}", end="--")
    print()
    print(f"Average Completion Time of Processes is {round(avgC,3)}")
    print(f"Average Turn Around Time of Processes is {round(avgT,3)}")
    print(f"Average Waiting Time of Processes is {round(avgW,3)}")


totalExecutionTime = 0


def main():
    global totalExecutionTime
    timeQuantum = 4
    totalExecutionTime = 0
    processes = createProcess()
    readyQ = []
    completionQ = []

    def complete(pro):
        global totalExecutionTime
        if pro.remainingBurstTime <= timeQuantum:
            totalExecutionTime += pro.remainingBurstTime
            pro.remainingBurstTime = 0
        else:
            pro.remainingBurstTime -= timeQuantum
            totalExecutionTime += timeQuantum
        completionQ.append(pro)
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

    for i in completionQ:
        i.calTurnaroundTime()
        i.calWaitingTime()

    dt = list(set(completionQ))
    dt.sort(key=lambda x: x.arrivalTime)
    printData(dt, completionQ)


main()
