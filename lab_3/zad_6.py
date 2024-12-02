def fib_gen(n):
    first = 0
    second = 1
    for i in range(n):
        yield first
        first, second = second, second + first


for fib in fib_gen(20):
    print(fib)

fib_num = fib_gen(10)
print(fib_num)
next(fib_num)