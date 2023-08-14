n = int(input())
l = list(map(int, input().split()))
stack = [1] * (n+1)

for i in range(len(l)):
    for j in range(i):
        if l[i] > l[j]:
            stack[i] = max(stack[i], stack[j]+1)
        
print(max(stack))
c = max(stack)

answer = []

for i in range(n-1, -1, -1):
    if stack[i] == c:
        answer.append(l[i])
        c -= 1
answer.reverse()
print(*answer)