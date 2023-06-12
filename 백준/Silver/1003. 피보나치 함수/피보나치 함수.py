n = int(input())

for _ in range(n):
    l = []
    l.append([1,0])
    l.append([0,1])
    a = int(input())
    for i in range(2,a+1):
        l.append([l[i-1][0] + l[i-2][0] , l[i-1][1] + l[i-2][1]])
    print(l[a][0], l[a][1])