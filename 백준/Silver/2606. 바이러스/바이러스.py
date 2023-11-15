V = int(input())
E = int(input())
MyMap=[[] for _ in range(V+1)]

for i in range(E):
    _from, _to = map(int,input().split())
    MyMap[_from].append(_to)
    MyMap[_to].append(_from)

for now in MyMap:
    now.sort()


def BFS(here):
    Q=[]
    Q.append(here)
    Visited[here]=True
    count = 0

    while Q:
        here=Q.pop(0)
        count+=1
        #print(here,end=' ')
        for next in MyMap[here]: # 234
            if not Visited[next]:
                Q.append(next)
                Visited[next]=True
    return count-1

Visited = [False]*(V+1)
result = BFS(1)
print(result)