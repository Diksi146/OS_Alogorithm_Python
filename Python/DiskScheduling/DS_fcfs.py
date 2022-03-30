
def fcfs_DS(diskQ, start_node):
    queue = []
    total_seek_time = 0
    for i in range(len(diskQ)):
        q = []
        if i == 0:
            q.append(diskQ[i])
            x = abs((diskQ[i]) - start_node)
            q.append(x)
            total_seek_time += x
            queue.append(q)
        else:
            q.append(diskQ[i])
            x = abs(diskQ[i] - diskQ[i - 1])
            q.append(x)
            total_seek_time += x
            queue.append(q)
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
