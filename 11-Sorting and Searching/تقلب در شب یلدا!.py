a = [int(i) for i in input().split()]
pool = [0]*100000
for i in range(0, len(a)):
    pool[a[i]] += 1
max = 0
for i in pool:
    if i > max:
        max = i
for i in range(0, 100000):
    if pool[i] == max:
        print(i, pool[i])
        break
