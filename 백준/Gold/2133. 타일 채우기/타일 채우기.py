n = int(input())

l = [0] * 31

l[2] = 3

for i in range(4, n+1,2):
    l[i] = l[i-2] * 3 + sum(l[:i-2]) * 2 + 2
print(l[n])