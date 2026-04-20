print("i am shashank")
a,b=10,20
print(f"a+b : {a+b}")
print(f"a-b : {a-b}")
print(f"a*b : {a*b}")
print(f"a/b : {a/b}")

print(f"a :{a}, b :{b}")
b,a=a,b
print(f"a :{a}, b :{b}")

name=input("name: ")
age=input("age: ")
study=input("what do you want to study: ")
print(f"helo  {name} you are  {age} years old and you  study the {study}")

s=input("santance:")
print(s.upper(),s.lower())
print(s.replace(" ","-"))
print(s.strip())

s=input("string")
print(len(s.replace(" ","")))

print("helo\n\tword\n")

a=int(input("enter the frist number: "))
b=int(input("enter the second number: "))
print(a>10 and b>10)
print(a<5)
print(not(a>5))

a = int(input("enter the age: "))
if a > 18:
    print("you are adult")
else:
     print("you are minor")
     
     
l=[1,2,3,4,5]
l.sort(reverse=True)
print(l)

l=[1,2,3,4,5]
print(l[::-1])


t = (1,2,3,4,5)
t[3]=2 

mf = {"apple", "banana", "cherry"}
ff = {"watermelon", "goa", "greps"}
mf.add("orange")
print(mf)
mf.remove("orange")
print(mf|ff)
print(mf&ff)

