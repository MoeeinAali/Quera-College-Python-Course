a = int(input())
b = int(input())
rev_a = a//100 + ((a//10)%10) * 10 + (a%10)* 100
rev_b = b//100 + ((b//10)%10) * 10 + (b%10)* 100
if rev_a < rev_b:
    print(a,'<',b)
elif rev_a > rev_b:
    print(b,'<',a)
else:
    print(a,'=',b)
