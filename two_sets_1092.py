n = int(input())
set1 = list()
set2 = list()

if n % 4 == 2 or n % 4 == 1:
    print('NO')
else:
    while n > 4:
        set1 += [n-3, n]
        set2 += [n-2, n-1]
        n -= 4
    else:
        if n == 3:
            set1 += [1, 2]
            set2 += [3]
        if n == 4:
            set1 += [1, 4]
            set2 += [2, 3]

    print('YES')
    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)