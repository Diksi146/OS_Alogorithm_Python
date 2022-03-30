
def fcfs_DS(diskQ, start_node):

    queue = []
    total_seek_time = 0
    node = start_node
    while len(diskQ) > 0:
        q = []
        diskQ.sort(key=lambda x: abs(x - node))
        q.append(diskQ[0])
        x = abs(diskQ[0] - node)
        total_seek_time += x
        q.append(x)
        queue.append(q)
        node = diskQ.pop(0)
    return [queue, total_seek_time]


def main():
    diskQ = []

    diskQ = list(map(int, input(
        "Enter The Disk Queue :").strip().split()))
    size = len(diskQ)
    start_node = int(input("Enter The Starting Node :- "))
    q = fcfs_DS(diskQ, start_node)
    print(q[0])
    print(f"total see time : {q[1]}")
    print(f" Average Seek Time : {q[1]/size}")


main()
