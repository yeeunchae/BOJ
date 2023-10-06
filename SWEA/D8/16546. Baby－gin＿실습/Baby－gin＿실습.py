howmany = int(input())
 
for tc in range(howmany):
    data = list(map(int, input().rstrip() ))
    Count = [0] * 10
    run1, triplet = 0, 0
 
    for i in range(len(data)):
        Count[data[i]] += 1
 
    for i in range(len(Count)): # OK
        if Count[i] >= 3 and Count[i]<6:
           triplet += 1
           Count[i] -= 3
        elif Count[i] == 6:
            triplet = 2
 
    for i in range(len(Count)-2):
        if Count[i] == 1 and Count[i+1] == 1 and Count[i+2] == 1:
            run1 += 1
            Count[i] -= 1
            Count[i+1] -= 1
            Count[i+2] -= 1
        elif Count[i] == 2 and Count[i+1] == 2 and Count[i+2] == 2:
            run1 = 2
 
    if run1+triplet>=2:
        print(f"#{tc+1} true")
    else:
        print(f"#{tc+1} false")