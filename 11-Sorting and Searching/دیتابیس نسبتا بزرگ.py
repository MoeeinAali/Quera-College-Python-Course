def seach_in_arrey(mylist, key):
    for i in range(len(mylist)):
        if mylist[i] == int(key):
            return 1

    return 0


n, q = map(int, input().split())
arrey = [int(i) for i in input().split()]
for i in range(q):
    p,q = input().split()
    q = int(q)
    print(seach_in_arrey(arrey,q))
