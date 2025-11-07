n = int(input())
num = list(map(int, input().split())) #input
num.append(1e9 + 1)
step = 0
minId = 0

for i in range(len(num)):
    if num[i] > num[minId]:
        for j in range(minId + 1, i):
            step += num[minId] - num[j]
        minId = i
print(step)