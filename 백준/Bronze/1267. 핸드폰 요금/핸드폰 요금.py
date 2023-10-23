n = int(input())
l = list(map(int, input().split()))

Y = 0
M = 0

for k in l:
    Y += ((k // 30)+1) * 10
    M += ((k // 60)+1) * 15
    
if Y > M:
  print('M', M)
elif Y == M:
    print('Y M', M)
else:
  print('Y', Y)
