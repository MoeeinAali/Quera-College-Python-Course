a = [0]*10
sum = 0
for i in range(10):
    a[i] = float(input())
    sum += a[i]
avr = sum / 10
cnt = 0
for i in range(10):
    if a[i] > avr:
        cnt += 1
print(cnt)
