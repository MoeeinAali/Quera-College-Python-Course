from math import factorial


def C(m, n):
    return factorial(m)//(factorial(n)*factorial(m-n))


a = int(input())
for i in range(a):
    for j in range(i+1):
        print(C(i, j), end=" ")
    print()
