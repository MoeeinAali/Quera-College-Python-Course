a, b = map(int, input().split())
if b < 11:
    print("Right ", end="")
else:
    print("Left ", end="")
print(10-a+1, end=" ")
if b > 10:
    print(b-10+1)
else:
    print(10-b+1)
