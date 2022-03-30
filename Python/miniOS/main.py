
from createProcesses import createProcess
from createProcesses import process
from createProcesses import printData
from fcfs import fcfs
from sjf import sjf
from sjf import sjfP
from rr import roundRobin
from priority import mainP


def main():
    flag = 1

    while flag:
        print("\n\t -----Welcome To The CPU Scheduling Algorithm App!!!!----- \n")
        print("\t Select Which Algorithm You Want To Execute")
        print("\t 1. First Come First Serve ")
        print("\t 2. Shortest Job First(Non-preemptive) ")
        print("\t 3. Shortest Job First(Preemptive) ")
        print("\t 4. Round Robin ")
        print("\t 5. Priority Scheduling ")
        print("\t 6. Press 0 to End The Application !")
        print()
        choice = int(input("Enter Your Choice :- "))
        if choice < 6:
            if choice == 0:
                flag = 0
                break
            else:
                if choice == 1:
                    # First Come First Serve Algorithm
                    print("First Come First Serve Algorithm Execution")
                    createProcess()
                    fcfs1 = fcfs(process.processes)
                    printData(fcfs1, fcfs1)
                elif choice == 2:
                    # Shortest Job First Algorithm
                    print("Shortest Job First Algorithm (Non Preemptive) Execution")
                    createProcess()
                    sjf1 = sjf(process.processes)
                    printData(sjf1, sjf1)
                elif choice == 3:
                    # Shortest Job First Preamptive
                    print("Shortest Job First Algorithm (Preemptive) Execution")
                    createProcess()
                    sjf2 = sjfP(process.processes)
                    printData(list(set(sjf2)), sjf2)
                elif choice == 4:
                    # Round Robin Algorithm
                    print("Round Robin Algorithm Execution")
                    createProcess()
                    rr1 = roundRobin(process.processes)
                    rrC = list(set(rr1))
                    rrC.sort(key=lambda x: x.processID)
                    printData(rrC, rr1)
                elif choice == 5:
                    # Round Robin Algorithm
                    print("\n\tPriority Scheduling Algorithm Execution")
                    mainP()
        else:
            print("Enter The Correct Choice !")
        process.processes.clear()


main()
