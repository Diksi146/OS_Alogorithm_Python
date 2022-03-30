# # OPP
# class PlayerCharacter:
#     # Class Object Attribute
#     membership = True
#     # consturctor Method

#     def __init__(self, name):
#         # Attributes or properties the object does have
#         self.name = name

#     def run(self):
#         print("run")


# player1 = PlayerCharacter("diksi")
# player2 = PlayerCharacter("diksi2")
# print(player1.name)
# print(player2.name)
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new = []
# for i in li:
#     if i <= 5:
#         new.append(i)
# print(new)
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
        self.remainingBurstTime = 0

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
    # def createProcess():
    #     p = input("Number of processes")
    #     for i in range(int(p)):
    #         processes.append(process(i, ran(1, 10), ran(1, 20)))
    #     for i in processes:
    #         print(f"{i.processID} {i.arrivalTime} {i.burstTime}")
    #     print("############")
    # createProcess()
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

p1 = process
# processes = []
# p = input("Number of processes")
# for i in range(int(p)):
#     process.processes.append(process(i, ran(1, 10), ran(1, 20)))

# for i in processes:
#     print(f"{i.processID} {i.arrivalTime} {i.burstTime}")


# p1 = process("P1", 0, 4)
# p1.calCompletionTime(1)
# print(p1.completionTime)
# print(p1.turnAroundTime)
