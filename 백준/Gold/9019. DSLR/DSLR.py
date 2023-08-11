from collections import deque

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    ch = [0] * 10001

    q = deque()

    q.append([a,''])

    while q:
        num,cmd = q.popleft()
        ch[num] = 1
        if num == b:
            print(cmd)
            break
        #D
        c = (num * 2) % 10000
        if ch[c] == 0:
            q.append([c,cmd + 'D'])
            ch[c] = 1

        #S
        c = (num-1) % 10000
        if ch[c] == 0:
            q.append([c,cmd + 'S'])
            ch[c] = 1
        
        #L
        c = ( (num*10) + (num//1000) )%10000
        if ch[c] == 0:
            q.append([c,cmd + 'L'])
            ch[c] = 1

        #R
        c = ( (num // 10) + ( (num%10) * 1000) )%10000
        if ch[c] == 0:
            q.append([c,cmd + 'R'])
            ch[c] = 1
