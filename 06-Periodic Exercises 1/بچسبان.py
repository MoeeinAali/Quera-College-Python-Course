n , k = map(int , input().split())
nums = list(map(int,input().split()))
exist = False
for i in nums:
    if i > k :
        exist = True
if exist:
    print("YES")
else:
    print("NO")