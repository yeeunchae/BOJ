
def DFS(here):
    way.append(here)
    Visited[here] = True

    for next in range(100):
        if MyMap[here][next] and not Visited[next]:
            DFS(next)

for tc in range(1, 11):
    MyMap = [[0 for _ in range(100)] for __ in range(100)]
    Visited = [False] * 100
    way = []
    first = 0
    _ = input() 

    Data = list(map(int, input().split()))
    howmany = len(Data) // 2  

    for j in range(howmany):
        start, stop = Data[j * 2], Data[j * 2 + 1]
        MyMap[start][stop] = 1

    DFS(0)

    if 99 in way:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
