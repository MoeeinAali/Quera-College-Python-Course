def maghloob(x):
    ans = 0
    while x> 0:
        ans = ans*10 + x%10
        x //= 10
    return ans
    
a = [0]
while True:
    s = input()
    if s=="End":
        break
    a.append(int(s))
    
for i in range(1,len(a)):
    print(maghloob(a[len(a)-i]))