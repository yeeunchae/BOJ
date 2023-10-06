def findNum(data):
    freq = [0]*101
    max_num=0

    for num in data:
        freq[num]+=1
        if freq[num] >= freq[max_num]:
            max_num = num
    return max_num

howmany=int(input())

for i in range(howmany):
    case = int(input())
    data = list(map(int,input().split()))
    manynum=findNum(data)
    print(f'#{i+1} {manynum}')