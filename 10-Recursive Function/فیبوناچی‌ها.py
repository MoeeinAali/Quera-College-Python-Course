def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input())
s = 0
for i in range(1, n + 1):
    s += fib(i)
print(s)