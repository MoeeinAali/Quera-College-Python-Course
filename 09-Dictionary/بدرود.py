mydict = {
    "Ahmadi": 2,
    "Bagheri": 4,
    "Mortazavi": 5,
    "Hosseini": 3,
    "Mahmoodi": 4
}

while (True):
    text = input()
    if text == "End":
        break
    else:
        text = text.split()
        # print(text, "***", mydict)
        if (text[0] in mydict.keys()) == False:
            print("Motasefane Shoma Davat Nistid!")
            continue
        else:
            if int(text[1]) > mydict[text[0]]:
                print("Tedade Afrade Davat Shode Kamtar Ast!")
                continue
            else:
                print("Khosh Amadid!")
                continue
