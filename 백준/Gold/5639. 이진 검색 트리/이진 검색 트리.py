import sys
sys.setrecursionlimit(10**5)

tree = []

while True:
    try:
        tree.append(int(sys.stdin.readline().rstrip()))
    except:
        break

def endtotop(root, end):
    
    if root > end:
        return
    
    right = end + 1

    for i in range(root + 1, end + 1):
        if tree[root] < tree[i]:
            right = i
            break

    endtotop(root + 1, right - 1)

    endtotop(right, end)

    print(tree[root])

endtotop(0,len(tree)-1)