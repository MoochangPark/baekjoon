n,m = map(int, input().split())

t = [] #체크판
k = [] #시작점별 누적

mins = 999999

def check(i,j):
    cnt1 = 0
    cnt2 = 0
    for y in range(i, i+8):
        for x in range(j, j+8):
            if (y+x) % 2 == 0:
                if t[y][x] != 'W':
                    cnt1 += 1
                if t[y][x] != 'B':
                    cnt2 += 1
            else:
                if t[y][x] != 'B':
                    cnt1 += 1
                if t[y][x] != 'W':
                    cnt2 += 1
    k.append(min(cnt1, cnt2))
    cnt1 = 0
    cnt2 = 0

for i in range(n):
    a = input()
    t.append(a)

for i in range(n-7):
    for j in range(m-7):
        check(i,j)
        mins = min(k)

print(mins)