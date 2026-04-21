def marrige(boy,girl):
    print(f"name  {girl}")
    print(f"name {boy}")
    print(f" {boy} married  {girl}")
marrige( "shashank","preethi")
marrige("shashank","nayana")


def tables(num):
    for i in range(1,10):
        print(f"{num}x{i}={num*i}")
tables(6)


def func(num):
     return int(str(num)*3)
a=100
b=func(10)
c=a+b
print(c)

def func(num):
    return int(str(num)*5)
a=3
b=func(10)
c=a+b
print(c)


def greet():
    print("hello world")
greet()

def greet_user(name):
    print(f"Hello {name}  welcome to python programming")
greet_user("shashank")

def add_num(a,b):
    for i in range(1,10):
        return (f"{a}+{b}={a+b}")
print(add_num(11,18))