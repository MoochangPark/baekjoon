import sys
sys.setrecursionlimit(10**5)

n = int(input())
inor = list(map(int, input().split()))
postor = list(map(int, input().split()))

tree = [0] * (n+1)

for i in range(n):
    tree[inor[i]] = i

def preor(ins, ine, pos, poe):
    if ins > ine or pos > poe:
        return
    root = postor[poe]

    left = tree[root] - ins
    right = ine - tree[root]

    print(root, end = " ")
    preor(ins, ins+left-1, pos, pos+left-1)
    preor(ine - right+1, ine, poe-right, poe-1)

preor(0,n-1,0,n-1)