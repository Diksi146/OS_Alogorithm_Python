
from queue import Queue
from tabulate import tabulate


def fifo(refQ, noRefQ, noFrames):
    frames = set()
    framesBox = []
    entryQ = Queue()
    noHit = 0
    noFaults = 0

    for i in range(noRefQ):
        if len(frames) == 0:
            frames.add(refQ[i])
            entryQ.put(refQ[i])
            noFaults += 1
        else:
            if refQ[i] not in frames:
                if len(frames) < noFrames:
                    frames.add(refQ[i])
                    entryQ.put(refQ[i])
                    noFaults += 1
                else:
                    item = entryQ.queue[0]
                    entryQ.get()
                    frames.remove(item)
                    frames.add(refQ[i])
                    entryQ.put(refQ[i])
                    noFaults += 1
            else:
                noHit += 1
        framesBox.append(list(frames))

    print(f" No of Hits = {noHit}")
    print(f" Hit Ratio = {noHit/noRefQ}")
    print(f" No of Faults = {noFaults}")
    print(f" Faults Ratio = {noFaults/noRefQ}")
    head = []
    for i in range(noFrames):
        head.append(f"f{i}")

    # head = ["f1", "f2", "f3"]
    print(tabulate(framesBox, headers=head, tablefmt="grid"))
    # print(framesBox)


def main():
    noFrames = int(input("Enter the number of Frames : "))
    refQ = list(
        map(int, input("Enter the elements of refQ: ").strip().split()))
    noRefQ = len(refQ)
    fifo(refQ, noRefQ, noFrames)


main()
