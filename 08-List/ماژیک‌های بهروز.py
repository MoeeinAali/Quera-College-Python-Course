n = int(input())
colors = [0] * (101)
inputs = list(map(int, input().split()))
min = n
for i in range(n):
    colors[inputs[i]] += 1
for i in range(1, 101):
    if colors[i] > 0 and colors[i] < min:
        min = colors[i]
for i in range(1, 101):
    if colors[i] == min:
        print(i)
        break
