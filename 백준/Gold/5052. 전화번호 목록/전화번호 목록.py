t = int(input())

for _ in range(t):
    n = int(input())

    l = []
    for _ in range(n):
        l.append(input())

    l.sort()

    def check():
        for i in range(n-1):
            if l[i]  == l[i+1][:len(l[i])]:
                return 'NO'
        return 'YES'
    answer = check()

    print(answer)