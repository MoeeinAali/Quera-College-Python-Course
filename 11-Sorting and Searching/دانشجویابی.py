n = int(input())
arrey = [int(i) for i in input().split()]
sum = 0
for i in range (len(arrey)):
    sum += arrey[i]

print(n*(n+1)//2 - sum)