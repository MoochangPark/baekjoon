ax,ay = map(int, input().split())
bx,by = map(int, input().split())
cx,cy = map(int, input().split())

t = (by-ay) * (cx-bx) - (cy-by) * (bx-ax)

if t > 0 :
    print(-1)
elif t == 0:
    print(0)
else:
    print(1)