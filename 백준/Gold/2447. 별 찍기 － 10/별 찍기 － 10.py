n = int(input())

def maketh(n):
    if n == 1:
        return ['*']

    t = maketh(n // 3)
    
    l = []
    for tt in t:
        l.append(tt * 3)
    for tt in t:
        l.append(tt + ' ' * (n // 3) + tt)
    for tt in t:
        l.append(tt * 3)
    
    return l

k = maketh(n)
print('\n'.join(k))