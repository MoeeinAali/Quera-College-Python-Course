str = input()
mylist = list(str)
n = len(mylist)*2 - 1
for i in range(1, n, 2):
    mylist.insert(i, "-")
for i in range(n):
    print(mylist[i], end="")
