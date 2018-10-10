def fib(x):
    if x == 1:
        return 1
    if x == 0:
        return 0
    else:
        return fib(x - 1) + fib(x-2)

print(fib(10))
print(fib(11))
print("Oh Boy!")