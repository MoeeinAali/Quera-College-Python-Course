n = int(input())
m = 0
while n > 0:
    m = 10*m + n % 10
    n = (n - n % 10)//10
print(m)
