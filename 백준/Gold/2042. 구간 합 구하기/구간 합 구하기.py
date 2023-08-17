n, m, k = map(int, input().split())

l = []
tree = [0] * 4000000

def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node]

for _ in range(n):
    l.append(int(input()))

init(1, 0, n-1)

def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff

    if start != end:
        update(node * 2, start, (start + end)//2, index, diff)
        update(node * 2+1, (start + end)//2+1, end, index, diff)

def subsum(node, start, end, left, right):

    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    return subsum(node*2, start, (start+end)//2, left, right) + subsum(node*2+1, (start+end)//2+1, end, left, right)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    
    if a == 1:
        b = b-1
        diff = c - l[b]
        l[b] = c
        update(1,0,n-1,b,diff)
    elif a == 2:
        print(subsum(1, 0, n-1, b-1, c-1))