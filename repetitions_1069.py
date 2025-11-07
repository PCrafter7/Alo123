string = input()
current = string[0]
count = 0
max = 0
for i in range(len(string)):
    if string[i] == current:
        count += 1
    else:
        current = string[i]
        if count > max:
            max = count
        count = 1
if count > max:
    max = count # in case the longest sequence is at the end
print(max)