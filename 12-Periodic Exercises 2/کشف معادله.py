import math


def function1(n: float):
    return n - math.floor(n)


def function2(n: float):
    return n**2 + n


def function3(n: float):
    return abs((-1)*n**3 + 1) + n**3


n = int(input())

x = []
y = []
for _ in range(n):
    a, b = map(float, input().split())
    x.append(a)
    y.append(b)

ans1 = [abs(function1(x[i]) - y[i]) for i in range(n)]
ans2 = [abs(function2(x[i]) - y[i]) for i in range(n)]
ans3 = [abs(function3(x[i]) - y[i]) for i in range(n)]


if max(ans1) <= 0.2:
    print(1)
if max(ans2) <= 0.2:
    print(2)
if max(ans3) <= 0.2:
    print(3)
if max(ans1) > 0.2 and max(ans2) > 0.2 and max(ans3) > 0.2:
    print("No ones")
