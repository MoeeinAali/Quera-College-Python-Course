def convert_to_base(n: int, b: int):
    if n == 0:
        return "0"

    digits = "0123456789ABCDEF"
    result = ""

    while n > 0:
        result = digits[n % b] + result
        n //= b

    return result


n, b = map(int, input().split())
print(convert_to_base(n, b))
