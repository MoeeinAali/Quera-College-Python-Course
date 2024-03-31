def squere(k, ch):
    global n
    if n > 0:
        for i in range(1, n+1):
            print(ch*n)
        n -= k
        squere(k, ch)
    else:
        return


n, k, ch = input().split()
n = int(n)
k = int(k)
squere(k, ch)
