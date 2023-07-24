from collections import deque

answer = -1

n, m = map(int, input().split())

l = []
check = []
Rr = []
Bb = []
Oo = []
for i in range(n):
    ll = list(input())
    for j in range(len(ll)):
        if ll[j] == 'R':
            Rr = [i,j]
        elif ll[j] == 'B':
            Bb = [i,j]
        elif ll[j] == 'O':
            Oo = [i,j]
    l.append(ll)

check.append(Rr)
my = [-1, 1, 0, 0]
mx = [0, 0, -1, 1]

def move(y, x, dy, dx):
    cnt = 0
    while l[y+dy][x+dx] != "#" and l[y][x] != "O":
        y += dy
        x += dx
        cnt += 1
    return y, x, cnt

q = deque()
q.append([Rr,Bb,0])

while q:
    t = 0
    r, b, count = q.popleft()

    if count >= 10:
        answer = -1
        t = 1
        break

    for dy, dx in zip(my, mx):
        rdy, rdx, rcnt = move(r[0],r[1],dy,dx)
        bdy, bdx, bcnt = move(b[0],b[1],dy,dx)

        if l[bdy][bdx] != 'O':
            if l[rdy][rdx] == 'O':
                answer = count + 1
                t = 1
                break
            if rdy == bdy and rdx == bdx:
                if rcnt > bcnt:
                    rdy -= dy
                    rdx -= dx
                else:
                    bdy -= dy
                    bdx -= dx
            if [rdy, rdx, bdy, bdx] not in check:
                check.append([rdy, rdx, bdy, bdx])
                q.append([[rdy, rdx], [bdy, bdx], count + 1])
    if t:
        break
print(answer)