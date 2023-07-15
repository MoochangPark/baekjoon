n = int(input())

l = list(map(int, input().split()))

stack = []
ans = [-1] * n
for idx, ll in enumerate(l):
    if len(stack):
        while len(stack) and l[stack[-1]] < ll:
            i = stack.pop()
            ans[i] = ll
    stack.append(idx)
print(*ans)