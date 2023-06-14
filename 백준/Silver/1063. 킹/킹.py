king, stone, move = map(str, input().split())

move_ctrl = {'R': (1,0), 'L': (-1,0), 'B': (0,-1), 'T': (0,1), 'RT': (1,1), 'LT': (-1,1), 'RB': (1,-1), 'LB': (-1,-1)}

king = [ord(king[0]) - 64, int(king[1:])]
stone = [ord(stone[0]) - 64, int(stone[1:])]
# print(king, stone)

for _ in range(int(move)):
    control = input()
    
    dy = king[0] + move_ctrl[control][0]
    dx = king[1] + move_ctrl[control][1]

    if 1 <= dy <= 8 and 1 <= dx <= 8: #king이 움직일 수 있을 떄
        if [dy,dx] == stone: #가는길에 돌이 있다면
            sy = stone[0] + move_ctrl[control][0]
            sx = stone[1] + move_ctrl[control][1]
            if 1 <= sy <= 8 and 1 <= sx <= 8: #돌도 움직일 수 있다면
                stone = [sy, sx]
                king = [dy, dx]
            else: #돌이 못움직이면
                continue
        else: #가는 길에 돌이 없다면
            king = [dy, dx]

print(chr(king[0] + 64) + str(king[1]))
print(chr(stone[0] + 64) + str(stone[1]))
