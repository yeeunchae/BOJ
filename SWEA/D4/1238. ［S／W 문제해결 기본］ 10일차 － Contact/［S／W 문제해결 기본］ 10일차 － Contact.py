for i in range(10):
    length,start = map(int, input().split())
    Data = list(map(int, input().split()))
    MyMap = [[0 for _ in range(101)] for __ in range(101)]
    Queue=[]
    Visited = [0] * 101
    distance = [0] * 101

    for j in range(0,length,2):
        MyMap[Data[j]][Data[j+1]] = 1
    Queue.append(start)
    while Queue:
        here = Queue.pop(0)
        Visited[here] = True
        for next in range(101):
            if MyMap[here][next] and not Visited[next] and next not in Queue:
                Queue.append(next)
                distance[next] = distance[here] + 1
    Max=[]
    for k in range(101):
        if max(distance) == distance[k]:
            Max.append(k)

    print(f'#{i+1} {max(Max)}')