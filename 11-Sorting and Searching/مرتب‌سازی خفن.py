n = int(input())
names = []
averages = []
sports = []
perm = []


for i in range(0, n):
    perm.append(i)
    name = input()
    names.append(name)
    data = input().split(" ")
    count = int(data[0])
    sum = 0
    for j in range(0, count):
        sum += float(data[j + 1])

    averages.append(sum / count)

    data = input().split(" ")
    count = int(data[0])

    sports.append(count)


def better(id1, id2):
    if int(averages[id1]) != int(averages[id2]):
        if averages[id1] > averages[id2]:
            return True
        return False
    if sports[id1] != sports[id2] :
        if(sports[id1] > sports[id2]):
            return True
        return False
    if id1 < id2:
        return True
    return False

for i in range(0, n - 1):
    for j in range(1, n):
        if(better(perm[j], perm[j - 1])):
            temp = perm[j]
            perm[j] = perm[j - 1]
            perm[j - 1] = temp

for i in range(0, n):
    print (names[perm[i]])

