a, b, c = input().split()
checker_s = 0
checker_star = 0
checker_7 = 0
if a == "s" or b == "s" or c == "s":
    checker_s = 1
if a == "*" or b == "*" or c == "*":
    checker_star = 1
if a == "7" or b == "7" or c == "7":
    checker_7 = 1

print(checker_s*10 + checker_7*5 + checker_star*30)
