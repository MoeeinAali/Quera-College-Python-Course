def func(n):
    if n == 0:
        return 5
    if n % 2 == 0:
        return func(n-1)-21
    else:
        return func(n-1)**2


a = int(input())
print(func(a))
