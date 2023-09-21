import sys
import math

n, m = map(int, sys.stdin.readline().split())

l = [int(sys.stdin.readline()) for _ in range(n)]

h = math.ceil(math.log2(n))+1
nodeNum = 1 << h
seg = [0] * nodeNum

def make_tree(idx,start,end):
    if start == end:
        seg[idx] = (l[start], l[start])
        return seg[idx]
    
    mid = (start + end) // 2

    left = make_tree(idx * 2, start, mid)
    right = make_tree(idx*2+1, mid+1, end)

    seg[idx] = [min(left[0], right[0]), max(left[1], right[1])]

    return seg[idx]


make_tree(1,0,len(l)-1)

def find(idx, start, end):
    if range2 < start or range1 > end:
        return (1000000000, 0)
    
    if range1 <= start and end <= range2:
        return seg[idx]
    
    mid = (start + end) // 2
    left = find(idx * 2, start, mid)
    right = find(idx * 2 + 1, mid + 1, end)
    return [min(left[0],right[0]), max(left[1],right[1])]

for _ in range(m):
    range1 ,range2 = map(int, sys.stdin.readline().split())
    range1 -= 1
    range2 -= 1
    answer = find(1,0,len(l)-1)
    print(answer[0],answer[1])