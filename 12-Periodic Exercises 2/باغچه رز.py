n, m = map(int, input().split())

inputs = []
for i in range(m):
    inputs.append(list(input()))

results = [0]*n

for i in range(n):
    cnt = 0
    for j in range(m):
        if inputs[j][i] == 'W':
            cnt += 1
    results[i] = cnt

for i in results:
    if i % 2 == 0:
        print('B', end="")
    else:
        print("F", end="")
