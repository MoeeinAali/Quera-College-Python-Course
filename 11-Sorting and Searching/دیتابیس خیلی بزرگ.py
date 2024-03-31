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


n, q = map(int, input().split())
arrey = [int(i) for i in input().split()]
for i in range(q):
    p,q = input().split()
    q = int(q)
    if binary_search(arrey,q)!=-1:
        print("1")
    else:
        print("0")
