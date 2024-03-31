n = int(input())
a = []
for i in range(n):
    inp = input().split()
    ch = inp[0]
    index = int(inp[1])

    if ch == '+':
        value = int(inp[2])
        a.insert(index - 1, value)
    else:
        a.pop(index - 1)
    
    if len(a) == 0:
        print("EMPTY")
    else:
        for x in a:
            print(x, end=' ')
        print()