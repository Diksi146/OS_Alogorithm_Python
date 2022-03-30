# Process Class

from tkinter import Grid
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

    def calCompletionTime(self, p):
        self.completionTime = p - self.burstTime

    def calTurnaroundTime(self):
        self.turnAroundTime = self.completionTime - self.burstTime

    def calWaitingTime(self):
        self.waitingTime = self.turnAroundTime - self.burstTime


def createProcess():
    processes = []
    p = input("Number of processes :- ")
    for i in range(int(p)):
        x, y = input(
            f"Enter the arrival time and burst time for {i+1}st process :- ").split()
        processes.append(process(i+1, int(x), int(y)))
    for i in processes:
        print(f"{i.processID} {i.arrivalTime} {i.burstTime}")
    print("############")
    return processes


def printQ(q):
    for i in q:
        print(f"{i.processID} {i.arrivalTime} {i.burstTime} {i.remainingBurstTime}")


def printData(queue):
    head = [
        "Process ID", "Arrival time", "Burst time",
        "Completion Time", "Turn Around Time", "Waiting Time"]
    print(tabulate(queue, headers=head, tablefmt=Grid))


totalExecutionTime = 0


def main():
    global totalExecutionTime
    timeQuantum = 4
    totalExecutionTime = 0
    processes = createProcess()
    readyQ = []
    completionQ = []

    def complete(pro):
        # totalExecutionTime = 0
        global totalExecutionTime
        if pro.remainingBurstTime <= timeQuantum:
            totalExecutionTime += pro.remainingBurstTime
            pro.remainingBurstTime = 0
            # print(t)
        else:
            pro.remainingBurstTime -= timeQuantum
            totalExecutionTime += timeQuantum
            # print(t)
        # totalExecutionTime = t
        print(f"{pro.remainingBurstTime} te = {totalExecutionTime}")
        # pro.remainingBurstTime = pro.remainingBurstTime - timeQuantum
        completionQ.append(pro)
        # Adding Processes to the ready queue
        if len(processes) > 0:  # check if processes queue is empty
            for i in processes:
                if i.arrivalTime <= totalExecutionTime:
                    # print(i.processID)
                    readyQ.append(i)
                    processes.pop(processes.index(i))
                    # print(f"{i.processID} appended")
        if pro.remainingBurstTime > 0:
            readyQ.append(pro)
        else:
            pro.completionTime = totalExecutionTime
        printQ(readyQ)
        print("------------")

    # Code for fist process to execute
    processes.sort(key=lambda x: x.arrivalTime)
    readyQ.append(processes.pop(0))
    complete(readyQ.pop(0))
    while len(readyQ) > 0:
        complete(readyQ.pop(0))

    # print(readyQ)
    # print(completionQ)
    for i in readyQ:
        print(f"{i.processID} {i.arrivalTime} {i.burstTime} {i.remainingBurstTime}")
    print("**********")
    for i in completionQ:
        print(f"{i.processID} {i.arrivalTime} {i.burstTime} {i.completionTime} {i.turnAroundTime} {i.waitingTime} {i.remainingBurstTime}")
    print("**********")
    print(totalExecutionTime)

    # printData(completionQ)


main()


# Aim : use various controls like edit, view, button, radio button, check boxes, autoCompleteText, image, button and toggle button on mobile to develope UI using android/ other.
