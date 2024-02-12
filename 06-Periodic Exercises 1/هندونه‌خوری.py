
w1, w2, w3, w4, w5 = map(int, input().split())

ans_i = 1
ans_w = w1

if w2 > ans_w:
    ans_i = 2
    ans_w = w2

if w3 > ans_w:
    ans_i = 3
    ans_w = w3

if w4 > ans_w:
    ans_i = 4
    ans_w = w4

if w5 > ans_w:
    ans_i = 5
    ans_w = w5

print(ans_i)
