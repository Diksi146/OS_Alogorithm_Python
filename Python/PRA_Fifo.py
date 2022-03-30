def main():
    global refQ
    global frames
    global framesBox
    global outS
    global hits
    global faults
    global noFrames
    noFrames = 0
    hits = 0
    faults = 0
    refQ = []
    frames = []
    framesBox = []
    outS = []

    def getData():
        noFrames = int(input("Enter the number of Frames : "))
        list1 = list(
            map(int, input("Enter the elements of refQ: ").strip().split()))
        return list1

    def fifo():
        # frames = []
        # framesBox = []
        global faults
        global hits
        global frames
        for i in refQ:
            print(frames)
            if len(frames) == 0:
                frames.append(i)
                outS.append(i)
                faults += 1
            else:
                for j in frames:
                    print("true")
                    if i == j:
                        print("true")
                        hits += 1
                        frames.append(i)
                        framesBox.append(frames)
                        break
                if len(frames) <= noFrames:
                    frames.append(i)
                    outS.append(i)
                    framesBox.append(frames)
                else:
                    n = outS.pop()
                    frames[frames.index(n)] = i
                    faults += 1
                    outS.append(i)
                    framesBox.append(frames)
    refQ = getData()
    fifo()
    print(refQ)
    print(faults)
    print(hits)

    print(framesBox)


main()
