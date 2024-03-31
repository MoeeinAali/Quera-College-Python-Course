def binary_search(arr, x):
    if arr[-1] == x:
        return len(arr) - 1
    if arr[-1] < x:
        return -1
    low = -1
    high = len(arr) -1

    while high - low > 1:
        middle = (low + high) // 2
        if arr[middle] <= x:
            low = middle
        else:
            high = middle
    if arr[low] == x:
        return low
    return -1

n = int(input())
arr = [int(i) for i in input().split()]
m = int (input())
ans = binary_search(arr, m)
print(ans)