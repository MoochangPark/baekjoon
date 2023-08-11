n = int(input())

l = list(map(int, input().split()))

ch = [0]

def search(target, start, end):
    while start <= end:
        p = (start + end) // 2
        if ch[p] == target:
            return p
        elif ch[p] < target:
            start = p + 1
        else:
            end = p - 1
    return start

for ll in l:
    if ch[-1] < ll:
        ch.append(ll)
    else:
        ch[search(ll,0,len(ch)-1)] = ll

print(len(ch) - 1)