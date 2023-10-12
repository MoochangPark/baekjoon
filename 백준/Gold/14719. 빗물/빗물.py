h, w = map(int, input().split())
l = list(map(int, input().split()))

answer = 0

for i in range(1,w-1):
    left = max(l[:i])
    right = max(l[i+1:])

    low = min(left, right)

    if l[i] < low:
        answer += low - l[i]
    
print(answer)