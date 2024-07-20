def isPrime(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    if cnt > 2:
        return False
    elif n == 1:
        return False
    else:
        return True


def jamArgham(n):
    sum = 0
    while (n > 0):
        sum += n % 10
        n //= 10
    return sum


def jamAvamel(n):
    sum = 0
    for i in range(1, n+1):
        if n % i == 0 and isPrime(i):
            sum += i
    return (sum)


def D(x):
    return jamArgham(x) + jamAvamel(x) + x


n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

D_Dict = dict()
nums_dict = dict()

for i in range(1, max(nums)+1):
    buff = D(i)
    nums_dict[i] = buff
    if buff in D_Dict:
        D_Dict[buff] += 1
    else:
        D_Dict[buff] = 1
for i in nums:
    if i in D_Dict:
        print("Yes")
    else:
        print("No")
