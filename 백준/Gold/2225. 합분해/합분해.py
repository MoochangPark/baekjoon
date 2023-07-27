from itertools import product

n, k = map(int, input().split())

check = [[0] * 201 for _ in range(201)]

for i in range(201):
    check[1][i] = 1
    check[2][i] = i + 1

for i in range(2,201):
    check[i][1] = i
    for j in range(2, 201):
        check[i][j] = (check[i-1][j] + check[i][j-1]) % 1000000000

print(check[k][n])