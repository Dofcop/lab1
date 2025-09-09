def fib_num(n):
    if n==1 or n==2:
        return 1
    if n==0:
        return 0
    return fib_num(n-1)+fib_num(n-2)