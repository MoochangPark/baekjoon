import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

answer = 0

start = 0
end = m

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in range(1,n+1):
        cnt += min(mid//i, n)

    if cnt >= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)