from collections import Counter

n, k = map(int, input().split())

answer = 0

words = [set(input()) for _ in range(n)]
learn = [0] * 26

for m in ('a', 'n', 't', 'i', 'c'):
    learn[ord(m) - ord('a')] = 1

def dfs(idx, count):
    global answer

    if count == k - 5:
        read = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                read += 1
        answer = max(answer, read)
        return
    
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, count + 1)
            learn[i] = False


dfs(0,0)
print(answer)