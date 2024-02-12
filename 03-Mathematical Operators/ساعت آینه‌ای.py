a, b = input().split()
a = int(a)
b = int(b)
print("%02d:%02d" % ((12 - a) % 12, (60 - b) % 60))