n = int(input())

alpha = []
alnum = {}
num = []

for i in range(n):
    alpha.append(input())

for i in range(n):
    for j in range(len(alpha[i])):
        if alpha[i][j] in alnum:
            alnum[alpha[i][j]] += 10 ** (len(alpha[i])-j-1)
        else:
            alnum[alpha[i][j]] = 10 ** (len(alpha[i])-j-1)

for v in alnum.values():
    num.append(v)

num.sort(reverse=True)

sum = 0
nums = 9
for i in num:
    sum += nums * i
    nums -= 1

print(sum)