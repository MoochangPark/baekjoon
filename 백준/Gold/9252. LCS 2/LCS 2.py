a = input()
b = input()

l = [[0] * (len(b)+1) for _ in range(len(a)+1)]
arr = [[''] * (len(b)+1) for _ in range(len(a)+1)]

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1] == b[j-1]:
            l[i][j] = l[i-1][j-1] + 1
            arr[i][j] = arr[i-1][j-1] + a[i-1]
        else:
            l[i][j] = max(l[i-1][j], l[i][j-1])
            if l[i-1][j] >= l[i][j-1]:
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = arr[i][j-1]

print(l[-1][-1])
if l[-1][-1] != 0:
    print(arr[-1][-1])