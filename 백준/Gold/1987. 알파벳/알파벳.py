r, c = map(int, input().split())

d = [0] * 26
l = []
for i in range(r):
    l.append(list(input()))
answer = 0
def dfs(sy,sx,count):
    global answer
    for y, x in ((0,1), (0,-1), (-1,0), (1,0)):
        dy = sy + y
        dx = sx + x
        if 0 <= dy < r and 0 <= dx < c:
            if d[ord(l[dy][dx]) - 65] == 0:
                d[ord(l[dy][dx]) - 65] = 1
                dfs(dy,dx,count+1)
                d[ord(l[dy][dx]) - 65] = 0

    answer = max(answer, count)

d[ord(l[0][0]) - 65] = 1
dfs(0,0,1)

print(answer)