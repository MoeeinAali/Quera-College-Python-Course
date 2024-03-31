ax, ay = input().split()
bx, by = input().split()
cx, cy = input().split()
dx = 0
dy = 0
if ax == bx:
    dx = cx
elif ax == cx:
    dx = bx
elif bx == cx:
    dx = ax
if ay == by:
    dy = cy
elif ay == cy:
    dy = by
elif by == cy:
    dy = ay

print(str(dx)+" "+str(dy))