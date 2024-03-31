n = int(input())
arr = [int(i) for i in input().split()]
for j in range(n):
    for k in range(n):
        if k+1 < n:
            if arr[k] < arr[k+1]:
                w = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = w
print(*arr)
