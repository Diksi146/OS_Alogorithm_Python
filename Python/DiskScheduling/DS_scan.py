
def Dsa_scan(diskQ, start_node, flag, diskSize):
    queue = []
    total_seek_time = 0
    node = start_node
    less_start_node = []
    greater_start_node = []
    for i in diskQ:
        if i >= start_node:
            greater_start_node.append(i)
        else:
            less_start_node.append(i)
    q = []
    if flag == 1:
        while greater_start_node:
            greater_start_node.sort(key=lambda x: x - node)
            x = abs(greater_start_node[0] - node)
            total_seek_time += x
            q.append(greater_start_node[0])
            q.append(x)
            queue.append(q.copy())
            node = greater_start_node.pop(0)
            q.clear()
        q.append(diskSize[1])
        q.append(abs(diskSize[1] - node))
        queue.append(q.copy())
        total_seek_time += abs(diskSize[1] - node)
        node = diskSize[1]
        q.clear()
        while less_start_node:
            less_start_node.sort(key=lambda x: x - node, reverse=True)
            x = abs(less_start_node[0] - node)
            total_seek_time += x
            q.append(less_start_node[0])
            q.append(x)
            queue.append(q.copy())
            node = less_start_node.pop(0)
            q.clear()
    if flag == 2:
        # greater_start_node.sort(key=lambda x: x, reverse=True)
        while less_start_node:
            less_start_node.sort(key=lambda x: x-node, reverse=True)
            x = abs(less_start_node[0] - node)
            total_seek_time += x
            q.append(less_start_node[0])
            q.append(x)
            queue.append(q.copy())
            node = less_start_node.pop(0)
            q.clear()
        q.append(node)
        q.append(abs(diskSize[0] - node))
        queue.append(q)
        total_seek_time += abs(diskSize[0] - node)
        node = diskSize[0]
        q.clear()
        while greater_start_node:
            greater_start_node.sort(key=lambda x: x-node)
            x = abs(greater_start_node[0] - node)
            total_seek_time += x
            q.append(greater_start_node[0])
            q.append(x)
            queue.append(q.copy())
            node = greater_start_node.pop(0)
            q.clear()

    return [queue, total_seek_time]


def main():
    diskQ = []

    diskQ = list(map(int, input(
        "Enter The Disk Queue :").strip().split()))
    start_node = int(input("Enter The Starting Node :- "))
    print("1.Outside")
    print("2.Inside")
    flag = int(input("Enter the direction of Nodes :"))
    diskSize = list(map(int, input("Enter the disk size : ").strip().split()))
    diskSize.sort(key=lambda x: x)
    stopFlag = 1
    while stopFlag:
        if flag == 1:
            q = Dsa_scan(diskQ, start_node, flag, diskSize)
            stopFlag = 0
        elif flag == 2:
            q = Dsa_scan(diskQ, start_node, flag, diskSize)
            stopFlag = 0
        else:
            print("Incorrect Direction Value!!!!")
    # q = Dsa_scan(diskQ, start_node)
    print(q[0])
    print(f"total see time : {q[1]}")
    print(f" Average Seek Time : {q[1]/len(q[0])}")


main()
