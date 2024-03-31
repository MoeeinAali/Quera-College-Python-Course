n, m = map(int, input().split())
a = [[0]*m for i in range(n)]
for i in range(n):
    a[i] = list(input())
    cnt = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == "*":
            cnt += 1

print(cnt)
