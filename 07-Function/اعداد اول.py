def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


a = int(input())
b = int(input())
for i in range(a, b+1):
    if is_prime(i):
        print(i)
