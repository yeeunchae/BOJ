def changeNum(data):
    max = 0
    min = 0
    for i in range(len(data)):
        if data[i]>=data[max]:
            max = i
        if data[i]<=data[min]:
            min = i
    data[max],data[min]=data[min],data[max]

howmany = int(input())
for i in range(howmany):
    data = list(map(int,input().split()))
    changeNum(data)
    print(f"#{i + 1} {' '.join(map(str, data))}")
