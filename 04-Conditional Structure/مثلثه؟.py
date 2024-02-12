a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if abs(a-b) < c and c < a+b:
    print("Bale")
else:
    print("Na")
