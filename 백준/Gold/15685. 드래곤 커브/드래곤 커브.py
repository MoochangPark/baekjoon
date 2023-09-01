n = int(input())

l = [[0] * (101) for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
for _ in range(n):
    y, x, d, g = map(int, input().split())
    l[x][y] = 1

    curve = [d]
    for i in range(g):
        for j in range(len(curve) - 1, -1, -1):
            curve.append((curve[j] + 1) % 4)

    for i in range(len(curve)):
        x += dx[curve[i]]
        y += dy[curve[i]]
        if 0 <= x < 101 and 0 <= y < 101:
            l[x][y] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if l[i][j] == 1 and l[i + 1][j] == 1 and l[i][j + 1] == 1 and l[i + 1][j + 1] == 1:
            answer += 1

print(answer)