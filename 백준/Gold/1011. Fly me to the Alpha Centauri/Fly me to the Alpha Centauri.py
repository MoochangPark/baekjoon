t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    d = b-a

    count = 0
    move = 1
    sum = 0
    while sum < d:
        count += 1
        sum += move
        if count % 2 == 0:
            move += 1
    print(count)