# Optimal Page replacement Algorithm
from tabulate import tabulate


def optimal(refQ, noRefElements, noFrames):
    framesBox = []
    noHits = 0
    noFaults = 0

    frames = set()
    outS = []

    for el in refQ:
        if len(refQ) == 0:
            frames.add(el)
            outS.append(el)
            noFaults += 1
        else:
            if el not in frames:
                if len(frames) < noFrames:
                    frames.add(el)
                    outS.append(el)
                    noFaults += 1
                else:
                    places = []
                    for fr in frames:
                        dist = 0
                        for place in range(refQ.index(el)+1, noRefElements):
                            dist += 1
                            distA = []
                            if fr == refQ[place]:
                                distA.append(refQ[place])
                                distA.append(dist)
                                places.append(distA)
                                break
                    places.sort(key=lambda x: x[1], reverse=True)
                    if len(places) == 0:
                        noFaults += 1
                    else:
                        frames.remove(places[0][0])
                        frames.add(el)
                        outS.append(el)
                        noFaults += 1
            else:
                noHits += 1
        framesBox.append(list(frames))

    print(f" No of Hits = {noHits}")
    print(f" Hit Ratio = {noHits/noRefElements}")
    print(f" No of Faults = {noFaults}")
    print(f" Faults Ratio = {noFaults/noRefElements}")
    head = []
    for i in range(noFrames):
        head.append(f"f{i}")
    print(tabulate(framesBox, headers=head, tablefmt="grid"))


def main():
    noFrames = int(input("Enter the no of frames : "))
    refQ = list(map(int, input("Enter the Elements of RefQ : ").strip().split()))
    noRefQ = len(refQ)
    optimal(refQ, noRefQ, noFrames)


main()
