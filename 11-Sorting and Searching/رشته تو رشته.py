s = input()
p = input()
for i in range(len(s) - len(p) + 1):
    flag = True
    for j in range(len(p)):
        if p[j] != s[i + j]:
            flag = False
    if flag:
        print(i + 1, end=' ')
print()