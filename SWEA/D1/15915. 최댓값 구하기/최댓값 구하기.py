
howmany = int(input())

for i in range(howmany):
    data = list(map(int, input().split()))
    max = -987654321

    for j in range(10):
        if data[j] > max:
            max = data[j]

    print(f"#{i+1} {max}")
