
for tc in range(1, 11):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]

    max = sum = 0
    for y in range(100):
        for x in range(100):
            sum += array[y][x]
        if max < sum : max = sum
        sum = 0

    for y in range(100):
        for x in range(100):
            if y > x:
                array[y][x], array[x][y] = array[x][y], array[y][x]

    for y in range(100):
        for x in range(100):
            sum += array[y][x]
        if max < sum : max = sum
        sum = 0

    for y in range(100):
        sum += array[y][y]
        if max < sum: max = sum
        sum = 0

    for y in range(100):
        sum += array[y][99 - y]
        if max < sum: max = sum

    print("#%d %d" %(tc, max))