from random import randint as ran


class process:
    processes = []

    def __init__(self, processID, arrivalTime, burstTime):
        self.processID = processID
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


def main():
    processes = []
    timeQuantum = 2
    executionTime = 0
    readyQ = []
    completeQ = []

    def createProcess():
        p = input("Number of processes :- ")
        for i in range(int(p)):
            x, y = input(
                f"Enter the arrival time and burst time for {i+1}st process :- ").split()
            processes.append(process(i, int(x), int(y)))
        for i in processes:
            print(f"{i.processID} {i.arrivalTime} {i.burstTime}")
        print("############")
    createProcess()

    processes.sort(key=lambda x: x.arrivalTime)
    readyQ.append(processes.pop(0))
    readyQ[0].remainingBurstTime = readyQ[0].burstTime - timeQuantum
    completeQ.append(readyQ.pop(0))
    # readyQ[0].remainingBurstTime = readyQ[0].burstTime - timeQuantum
    executionTime = 2
    for pro in processes:
        if pro.arrivalTime <= executionTime:
            readyQ.append(pro)
    if completeQ[0].remainingBurstTime > 0:
        readyQ.append(completeQ[0])
    readyQ.sort(key=lambda x: x.burstTime)
    completeQ.append(readyQ.pop(0))
    executionTime = executionTime + completeQ[len(completeQ - 1)].burstTime

    for i in processes:
        print(f"{i.processID} {i.arrivalTime} {i.burstTime}")
    print("------------")
    for i in completeQ:
        print(f"{i.processID} {i.arrivalTime} {i.burstTime}")
    print("---------------")
    for i in readyQ:
        print(f"{i.processID} {i.arrivalTime} {i.burstTime}")
    print(readyQ[0].remainingBurstTime)


main()

# def createProcess():
#     p = input("Number of processes")
#     for i in range(int(p)):
#         processes.append(process(i, ran(1, 10), ran(1, 20)))
#     for i in processes:
#         print(f"{i.processID} {i.arrivalTime} {i.burstTime}")
#     print("############")
# createProcess()


def executeSjfp(processes):
    readyQ = []
    completeQ = []
    timeQuantum = 2
    processes.sort(key=lambda x: x.arrivalTime)
    executionTime = timeQuantum
    readyQ.append(processes)
    completeQ.append(processes.pop(0))
    readyQ[len(readyQ)-1].remainingBurstTime -= timeQuantum
    completeQ[len(completeQ)-1].remainingBurstTime -= timeQuantum
    while len(processes):
        for pro in processes:
            if pro.arrivalTime <= executionTime:
                readyQ.append(pro)
                processes.remove(pro)
        if completeQ[len(completeQ)-1] > 0:
            readyQ.sort(lambda x: x.remainingTime)
            if readyQ[0].remainingBurstTime == completeQ[len(completeQ)-1].remainingBurstTime:
                completeQ.append(completeQ[len(completeQ)-1])
                break
            else:
                readyQ.append(completeQ[len(completeQ)-1])
        readyQ.sort(lambda x: x.remainingTime)
        completeQ.append(readyQ.pop(0))
        completeQ[len(completeQ)-1].remainingBurstTime -= timeQuantum
    else:
        if len(readyQ):
            for i in range(len(readyQ)):
                readyQ.sort(lambda x: x.remainingTime)
                completeQ.append(readyQ.pop(0))
