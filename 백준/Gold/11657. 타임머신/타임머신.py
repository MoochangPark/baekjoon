n, m = map(int, input().split())
l = [21E8] * (n+1)

d = []
for _ in range(m):
    a, b, c = map(int, input().split())
    d.append((a,b,c))

def bf(start):
    l[start] = 0
    for i in range(n):
        for j in range(m):
            node = d[j][0]
            next_node = d[j][1]
            cost = d[j][2]

            if l[node] != 21E8 and l[next_node] > l[node] + cost:
                l[next_node] = l[node] + cost

                if i == n-1:
                    return True
    return False

cycle = bf(1)

if cycle:
    print(-1)
else:
    for i in range(2,n+1):
        if l[i] == 21E8:
            print(-1)
        else:
            print(l[i])