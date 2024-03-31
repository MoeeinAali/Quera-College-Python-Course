a_cnt = 0
b_cnt = 0
c_cnt = 0
while True:
    a, b, c = map(int, input().split())
    if a == b and b == c:
        break
    else:
        d = min(a, b, c)
        cnt = 0
        if a == d:
            cnt += 1
        if b == d:
            cnt += 1
        if c == d:
            cnt += 1

        if cnt == 1:
            if a == d:
                a_cnt += 1
            if b == d:
                b_cnt += 1
            if c == d:
                c_cnt += 1
if a_cnt > b_cnt and a_cnt > c_cnt:
    print("Eyval Bijan!")
else:
    print("Ey baba! Eshkal nadare.")
