names = input().split()
mydict = {}

for name in names:
    mydict[name] = 0

while True:
    text = input()
    if text == "End":  
        break
    else:
        text = text.split()
        mydict[text[0]] += int(text[1])

values_list = list(mydict.values())
maxvalue = max(values_list) 

for key, value in mydict.items(): 
    if value == maxvalue:
        print(key)
