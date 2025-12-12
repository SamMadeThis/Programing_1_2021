import sys
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

##fibo.fib(1000)
#importing fib function and calling fibo?
##fibo.fib(1000)

##fibo.fib2(100)
##
##fibo.__name__
##
###assigning a function a local name
##fib = fibo.fib

