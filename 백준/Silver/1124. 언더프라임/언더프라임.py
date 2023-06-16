A, B = map(int, input().split())
ans = 0

array = [False, False] + [True for i in range(2,B+1)] #소수 판별

for i in range(2, int(B**0.5) + 1):
    if array[i] == True:
        j = 2
        while i * j <= B:
            array[i*j] = False
            j += 1

data = [0 for _ in range(B + 1)]

for i in range(1, B+1):
    if array[i]:
        data[i] = 1

for i in range(2, B+1):
    for j in range(2, B+1):
        if i * j > B:
            break
        else:
            if array[j]:
                data[i*j] = data[i] + 1

for i in range(A, B + 1):
    if array[data[i]]:
        ans += 1

print(ans)
