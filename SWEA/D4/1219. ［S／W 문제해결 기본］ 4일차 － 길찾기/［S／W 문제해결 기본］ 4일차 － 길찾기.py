def DFS(here):
    way.append(here)
    Visited[here]=True

    for next in range(100):
        if MyMap[here][next] and not Visited[next]:
            DFS(next)

for tc in range(1,11):
    MyMap = [[0 for _ in range(100)] for __ in range(100)]
    Visited = [False]*100
    way=[]
    _ = input()

    Data = list(map(int,input().split()))
    V = len(Data) // 2

    for i in range(V):
        start,stop = Data[i*2],Data[i*2+1]
        MyMap[start][stop] = 1

    DFS(0)

    if 99 in way:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

