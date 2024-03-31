En = {"1":"One","2":"Two","3":"Three","4":"Four","5":"Five"}
Fr = {"1":"Un","2":"Deux","3":"Trois","4":"Quatre","5":"Cinq"}

while(True):
    text = input()
    if text == "End":
        break
    else:
        text = text.split()
        if text[1] == "En":
            print(En[text[0]])
        else:
            print(Fr[text[0]])
        