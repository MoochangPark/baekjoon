import heapq
import sys

n = int(sys.stdin.readline())
maxh = [] #왼쪽 - 왼쪽은 첫번쨰로 나오는애가 중앙값
minh = []
for i in range(n):
    t = int(sys.stdin.readline())

    if len(maxh) == len(minh):
        heapq.heappush(maxh,-t)
    else:
        heapq.heappush(minh,t)
    
    if len(minh) and -maxh[0] > minh[0]:
        mxv = heapq.heappop(maxh)
        mnv = heapq.heappop(minh)

        heapq.heappush(maxh,-mnv)
        heapq.heappush(minh,-mxv)

    print(-maxh[0])