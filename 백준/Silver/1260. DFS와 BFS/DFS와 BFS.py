V,E,start = map(int,input().split()) #V=4, E=5, start=1

MyMap=[[] for _ in range(V+1)]

for i in range(E):
    _from, _to = map(int,input().split())
    MyMap[_from].append(_to)
    MyMap[_to].append(_from)

for now in MyMap:
    now.sort()

def DFS(here):
    print(here,end=' ')
    Visited[here]=True
    for next in MyMap[here]:
        if not Visited[next]:
            DFS(next)

def BFS(here):
    Q=[]
    Q.append(here)
    Visited[here]=True

    while Q:
        here=Q.pop(0)
        print(here,end=' ')
        for next in MyMap[here]: # 234
            if not Visited[next]:
                Q.append(next)
                Visited[next]=True


Visited = [False]*(V+1)
DFS(start)
print()
Visited = [False]*(V+1)
BFS(start)