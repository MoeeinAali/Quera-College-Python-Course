mydict = {}

while True:
    text = input()
    if text == "End":
        break
    else:
        text = text.split()
        mydict[text[0]] = float(text[1])

avr = sum(mydict.values()) / len(mydict.values())
mylist = [key for key, value in mydict.items() if value >= avr]

print(mylist)

summ = sum(mydict[key] for key in mylist)
cnt = len(mylist)


average = summ / cnt
print( average)

