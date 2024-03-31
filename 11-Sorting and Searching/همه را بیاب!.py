n = int(input())
arrey = [int(i) for i in input().split()]
checker = False
m = int(input())
for i in range(len(arrey)):
    if arrey[i] == m:
        print(i, end=" ")
        checker = True

if checker == False:
    print("-1")
