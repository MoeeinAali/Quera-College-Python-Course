x = int(input())
saat = int(x // 3600)
daghigheh = int((x % 3600) / 60)
sanieh = int(x - saat * 3600 - daghigheh * 60)
print(saat, " : ", daghigheh, " : ", sanieh)