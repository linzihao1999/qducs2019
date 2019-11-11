def fib(x):
    if x == 1 or x == 2:
        return 1
    return fib(x - 1) + fib(x - 2)


n = int(input())
for i in range(1, n + 1):
    print(fib(i))
