n, m, sy, sx, k = map(int, input().split())

l = []
for i in range(n):
    ll = list(map(int, input().split()))
    l.append(ll)

dice = [0,0,0,0,0,0]
def turn(act):
    global dice
    # 동쪽
    if act == 1:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    # 서쪽
    elif act == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    # 북쪽
    elif act == 3:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    # 남쪽
    else:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

dy= [0,0,-1,1]
dx = [1,-1,0,0]

action = list(map(int, input().split()))
y, x = sy, sx
for a in action:

    if 0 <= y+dy[a-1] < n and 0 <= x+dx[a-1] < m:
        y += dy[a-1]
        x += dx[a-1]
        turn(a)
        
        if l[y][x] == 0:
            l[y][x] = dice[-1]
        else:
            dice[-1] = l[y][x]
            l[y][x] = 0
        print(dice[0])