def solve(k):
    if k == 1:
        return 1
    elif k % 2 == 0:
        return 2 * solve(k / 2) - 1
    else:
        return 2 * solve((k - 1) / 2) + 1

n = int(input())
print(solve(n))