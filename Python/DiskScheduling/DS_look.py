queue = []
total_seek_time = 0
node = 0


def greater(greater_start_node):
    global node
    global total_seek_time
    global queue
    q = []
    while greater_start_node:
        greater_start_node.sort(key=lambda x: x - node)
        x = abs(greater_start_node[0] - node)
        total_seek_time += x
        q.append(greater_start_node[0])
        q.append(x)
        queue.append(q.copy())
        node = greater_start_node.pop(0)
        q.clear()


def less(less_start_node):
    global node
    global total_seek_time
    global queue
    q = []
    while less_start_node:
        less_start_node.sort(key=lambda x: x - node, reverse=True)
        x = abs(less_start_node[0] - node)
        total_seek_time += x
        q.append(less_start_node[0])
        q.append(x)
        queue.append(q.copy())
        node = less_start_node.pop(0)
        q.clear()


def fcfs_DS(diskQ, start_node, flag, diskSize):
    global node
    global total_seek_time
    global queue
    node = start_node
    less_start_node = []
    greater_start_node = []
    for i in diskQ:
        if i > start_node:
            greater_start_node.append(i)
        else:
            less_start_node.append(i)
    q = []

    if flag == 1:
        greater(greater_start_node)
        q.append(diskSize[1])
        q.append(abs(diskSize[1] - node))
        queue.append(q.copy())
        total_seek_time += abs(diskSize[1] - node)
        node = diskSize[1]
        q.clear()
        less(less_start_node)

    if flag == 2:
        less(less_start_node)
        q.append(node)
        q.append(abs(diskSize[0] - node))
        queue.append(q)
        total_seek_time += abs(diskSize[0] - node)
        node = diskSize[0]
        q.clear()
        greater(greater_start_node)


def main():
    diskQ = []

    diskQ = list(map(int, input(
        "Enter The Disk Queue :").strip().split()))
    size = len(diskQ)
    start_node = int(input("Enter The Starting Node :- "))
    print("1.Outside")
    print("2.Inside")
    flag = int(input("Enter the direction of Nodes :"))
    diskSize = list(map(int, input("Enter the disk size : ").strip().split()))
    diskSize.sort(key=lambda x: x)
    notCorrect = 1
    while notCorrect:
        if flag == 1:
            fcfs_DS(diskQ, start_node, flag, diskSize)
            notCorrect = 0
        elif flag == 2:
            fcfs_DS(diskQ, start_node, flag, diskSize)
            notCorrect = 0
            pass
        else:
            print("Incorrect Direction Value!!!!")
    print(queue)
    print(f"total see time : {total_seek_time}")
    print(f" Average Seek Time : {total_seek_time / size}")


main()
