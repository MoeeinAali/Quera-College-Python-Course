def fib(n, array):
    if(n == 1):
        if(array[n] == 0):
            array[n] = 1
        return array[n]
    if(n == 2):
        if(array[n] == 0):
            array[n] = 2
        return array[n]
    if(array[n] == 0):
        array[n] = fib(n - 1, array) + fib(n - 2, array)
    return array[n]

n = int(input())
array = [0 for i in range(n + 1)]
print(fib(n, array))