def squere(n):
    for i in range(1, n+1):
        print("*"*n)


def func1(n):
    for i in range(1, n+1):
        print((n+1-i)*"*")


n, ch = input().split()
n = int(n)
if ch == 's':
    squere(n)
else:
    func1(n)
