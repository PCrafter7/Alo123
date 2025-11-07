def spiral(row, column):
    if column % 2 == 1:
        return column**2 - (row - 1)
    else:
        return (column - 1)**2 + row

t = int(input())

coor = list()
for _ in range(t):
    coor += list(map(int,input().split()))

for i in range(0, len(coor), 2):
    print(spiral(coor[i], coor[i+1]))