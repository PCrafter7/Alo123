n = int(input())
zeros = 0
k = 1
while 5 ** k <= n:
    for i in range(1, n):
        zeros += 1 if i % 5**k == 0 else 0
    k += 1
print(k)