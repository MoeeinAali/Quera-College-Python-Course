a = list()

for i in range(10):
    x = int(input())
    a.append(x) 

for i in range(10):
    if i < 9:
        print(a[10 - i - 1],end='-')
    else:
        print(a[10 - i - 1])