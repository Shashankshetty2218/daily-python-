add = lambda a,b :a+b
print(add(1,5))

double =lambda x:2*x
print(double(300))

def calculate(n):
    if n==1:
        return 1
    return n* calculate(n-1)
print(calculate(3))

def num(*args):
    if not args:
        return 5
    return sum(args)
print(num(3,4,1))