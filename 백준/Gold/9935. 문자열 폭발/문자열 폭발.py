l = list(input())
r = input()

s = []
lr = len(r)
for ll in l:
    s.append(ll)
    if ''.join(s[-lr:]) == r:
        for _ in range(lr):
            s.pop()
if len(s):
    print(''.join(s))
else:
    print("FRULA")