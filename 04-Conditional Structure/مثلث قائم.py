a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
cnt = 0
if a == 90:
    cnt += 1
if b == 90:
    cnt += 1
if c == 90:
    cnt += 1
if cnt == 1:
    print("Bale")
else:
    print("Na")
