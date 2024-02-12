a, b, c = input().split()
num1, num2, num3 = input().split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
if a==b:
    print("Max : "+str(max(num1,num2,num3)))
elif a==c:
    print("Min : "+str(min(num1,num2,num3)))
else:
    print("None")