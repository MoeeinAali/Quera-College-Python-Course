def isPrime(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    if cnt > 2:
        return False
    else:
        return True


a = int(input())
b = int(input())
nums = []
for i in range(a+1, b):
    if isPrime(i):
        nums.append(str(i))

print(",".join(nums))
