from multiprocessing import ProcessError


class process:
    processes = []
    executionSequence = []
    availableResources = []

    def __init__(self, processID):
        self.processID = "P" + str(processID)
        self.allocatedR1 = 0
        self.allocatedR2 = 0
        self.allocatedR3 = 0
        self.maxR1 = 0
        self.maxR2 = 0
        self.maxR3 = 0

    def calRequired(self):
        r1 = self.maxR1 - self.allocatedR1
        r2 = self.maxR2 - self.allocatedR2
        r3 = self.maxR3 - self.allocatedR3
        self.required = [r1, r2, r3]


def main():
    noPro = int(input("Enter the Number of Prcosesse :- "))
    for i in range(noPro):
        pro = process(i)
        x, y, z = input(
            f"Enter the Resource Allocatio R1 R2 and R3 for Process {i+1} :- ").split()
        pro.allocatedR1 = int(x)
        pro.allocatedR2 = int(y)
        pro.allocatedR3 = int(z)
        process.processes.append(pro)

    for i in process.processes:
        x, y, z = input(
            f"Enter the Max Resource Required R1 R2 and R3 for process :- ").split()
        i.maxR1 = int(x)
        i.maxR2 = int(y)
        i.maxR3 = int(z)

    for i in process.processes:
        i.calRequired()
        print(
            f"{i.allocatedR1}-{i.allocatedR2}-{i.allocatedR3}-{i.maxR1}-{i.maxR2}-{i.maxR3}")

    x, y, z = input("Enter the available Resources R1, R2, R3 :- ").split()
    process.availableResources.append(int(x))
    process.availableResources.append(int(y))
    process.availableResources.append(int(z))
    # while len(process.processes) > 0:
    #     for i in process.processes:
    #         print("hiii")
    #         if i.required[0] <= process.availableResources[0]:
    #             if i.required[1] <= process.availableResources[1]:
    #                 if i.required[2] <= process.availableResources[2]:
    #                     print("stage 12")
    #                     process.executionSequence.append(i.processID)
    #                     process.availableResources[0] += i.allocatedR1
    #                     process.availableResources[1] += i.allocatedR2
    #                     process.availableResources[2] += i.allocatedR3
    #                     process.processes.remove(i)
    #                     break

    while len(process.processes) > 0:
        for i in process.processes:
            print("hiii")
            print(i.required[0])
            print(i.required[1])
            print(i.required[2])
            print("-----")
            print(process.availableResources[0])
            print(process.availableResources[1])
            print(process.availableResources[2])
            if i.required[0] <= process.availableResources[0]:
                if i.required[1] <= process.availableResources[1]:
                    if i.required[2] <= process.availableResources[2]:
                        print("stage 12")
                        process.availableResources[0] = process.availableResources[0] + i.allocatedR1
                        process.availableResources[1] = process.availableResources[1] + i.allocatedR2
                        process.availableResources[2] = process.availableResources[2] + i.allocatedR3
                        process.executionSequence.append(i.processID)
                        pro = i
                        break
        if pro:
            process.processes.remove(pro)
    for i in process.executionSequence:
        print(i)


main()
