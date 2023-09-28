n, m = map(int, input().split())

bite = [0] + list(map(int, input().split()))

none = [0] + list(map(int, input().split()))

bag = [[0] * (sum(none)+1) for _ in range(n+1)]

answer = sum(none)

for i in range(1, n+1):
    weight = bite[i]
    value = none[i]

    for j in range(1, sum(none)+1):
        if j < value:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(weight + bag[i-1][j-value], bag[i-1][j])

        if bag[i][j] >= m:
            answer = min(answer, j)
            
print(answer)