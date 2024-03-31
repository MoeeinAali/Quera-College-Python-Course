num = list(map(int,input().split()))
max = num[0]
min = num[0]

for a in num:
    if max < a:
        max = a
    if min > a:
        min = a

print('MAX: ', max)
print('MIN: ', min)