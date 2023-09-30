t = int(input())
for _ in range(t):
    answer = 0
    parent = {}
    counter = {}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a,b):
        A = find(a)
        B = find(b)

        if A != B:
            parent[B] = A
            counter[A] += counter[B]

    f = int(input())
    for i in range(f):
        a,b = input().split()

        if a not in parent:
            parent[a] = a
            counter[a] = 1
        if b not in parent:
            parent[b] = b
            counter[b] = 1

        union(a,b)

        print(counter[parent[a]])