K = int(input())
num = []
for i in range(1,K+1):
    a = int(input())
    if a == 0:
        num.pop()
    else:
        num.append(a)


sum = 0
for i in range(len(num)):
    sum += num[i]
print(sum)