from itertools import combinations

n, k  = map(int, input().split())
l = [i for i in range(1,n+1)]
answer = 0
for i in combinations(l,k):
    answer += 1
print(answer)