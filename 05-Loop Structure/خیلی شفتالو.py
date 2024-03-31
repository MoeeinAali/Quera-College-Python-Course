a = int(input())
sum = 0
for i in range(1, a+1):
    print("\n"+str(1), end="")
    if i > 1:
        for j in range(2, i+1):
            print("+"+str(j), end="")
    sum += i*(i+1)//2
    print(" = "+str(i*(i+1)//2), end="")
    
print("\nTotal sum of series is: "+str(int(sum)))