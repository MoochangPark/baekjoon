l = list(input())
answer = 0
stack = []
im = 1
for i in range(len(l)):
    if l[i] == '(':
        im *= 2
        stack.append(l[i])
    elif l[i] == '[':
        im *= 3
        stack.append(l[i])
    elif l[i] == ')':
        if not stack or stack[-1] != '(':
            answer = 0
            break
        if l[i-1] == '(':
            answer += im
        im //= 2
        stack.pop()
    elif l[i] == ']':
        if not stack or stack[-1] != '[':
            answer = 0
            break
        if l[i-1] == '[':
            answer += im
        im //= 3
        stack.pop()
if stack:
    print(0)
else:
    print(answer)