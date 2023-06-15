n, y, x = map(int, input().split())


ans = 0

while n != 0:
    #먼저 하나 작은 사이즈로 만들어본다
    n -= 1
    size = 2 ** n

    if y < size and x < size:
        ans += 0

    elif y < size and x >= size:
        ans += size * size
        x -= size
    
    elif y >= size and x < size:
        ans += size * size * 2
        y -= size

    elif y >= size and x >= size:
        ans += size * size * 3
        y -= size
        x -= size
        
print(ans)