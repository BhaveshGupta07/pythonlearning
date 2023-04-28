def fib(range):
    x,y=0,1
    while x < range:
        yield x
        x,y= y , x+y

a=fib(12)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))