l = list(input())
g = []
for i in range(1,len(l)-1):
  for j in range(i+1,len(l)):
    a = l[:i]
    b = l[i:j]
    c = l[j:]
    a.reverse()
    b.reverse()
    c.reverse()
    
    t = a+b+c
    g.append(''.join(t))
print(sorted(g)[0])