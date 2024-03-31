n, x = map(int, input().split())
arrey = [0]*n
arrey = list(map(int, input().split()))
arrey2 = [0]*n
for i in range(n):
    arrey2[(i+x) % n] = arrey[i]
for i in range(n):
    print(arrey2[i], end=" ")
