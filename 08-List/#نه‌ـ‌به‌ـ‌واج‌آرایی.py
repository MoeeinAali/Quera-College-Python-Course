def func1(input):
    a = 58*[0]
    string = list(input)
    for i in range(len(string)):
        a[ord(string[i])-65] = 1
    cnt = 0
    for i in range(len(a)):
        if a[i] != 0:
            cnt += 1
    return cnt


number = int(input())
max = -999
for i in range(number):
    inputt = input()
    buff = func1(inputt)
    if buff > max:
        max = buff

print(max)
