
def main():
    # global processes
    # global memmoryBlock
    processes = []
    memmoryBlock = []
    pro = input("Enter the No of processes :- ")
    for i in range(int(pro)):
        process = []
        process.append(i+1)
        process.append(
            int(input(f"Enter the size of process for {i+1} :-")))
        processes.append(process)
        print(process)
    noBlock = input("Enter the No of Memmory Blocks :- ")
    for i in range(int(noBlock)):
        block = []
        block.append(i+1)
        block.append(
            int(input(f"Enter the size of {i+1} memory block for :-")))
        block.append(block[1])
        memmoryBlock.append(block)
        print(block)

    # pro[0] = index no of process, p[1] = size of process.
    for pro in processes:
        for block in memmoryBlock:
            if pro[1] <= block[1]:
                pro.append(block[0])
                block[1] -= pro[1]
                break
    for i in processes:
        print(
            f" Process p{i[0]} is of size {i[1]} allocated in memmory block {i[2]}")
    for i in memmoryBlock:
        print(
            f"Memmory block {i[0]} has left blank memmory {i[1]} and it has allocated {i[2]}")


main()
