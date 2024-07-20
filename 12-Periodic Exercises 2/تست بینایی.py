n = input()
a = list(input())
b = list(input())
cnt = 0
for i in range(len(a)):
    if a[i] != b[i]:
        cnt += 1
print(cnt)
