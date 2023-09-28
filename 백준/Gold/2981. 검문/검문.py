from math import gcd

n = int(input())
l = [int(input()) for _ in range(n)]

l.sort() #최대공약수를 편하게 하기 위한 정렬

t = []
for i in range(1, n):
    t.append(l[i] - l[i-1]) # 앞수에서 전수를 뺴는 패던이 있음
    # A = M*a+R, B = M*b+R 이므로 A-b = M(a-b)가 성립
    #고로 이들의 최대공약수로 나누면 나누어 떨어지든 아니든 나머지가 같아짐

temp = t[0] #모든 수의 최대공약수

for i in range(1, len(t)):
    temp = gcd(temp, t[i])

answer = []
for i in range(2, int(temp**0.5)+1):
    if temp % i == 0:
        answer.append(i)
        answer.append(temp//i)
answer.append(temp)
answer = list(set(answer))
answer.sort()
print(*answer)