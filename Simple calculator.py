def a(x,y):
    return x + y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        return "Can't divide by zero!"
    return x/y
x=int(input("Enter a number X:"))
y=int(input("Enter a number Y:"))
op=input("Enter the operator (+,-,x,/):")
if op=="+":
    z=a(x,y)
elif op=="-":
    z=sub(x,y)
elif op=="X"or"x":
    z=mul(x,y)
elif op=="/":
    z=div(x,y)
print("Answer ",x,op,y,"=",z)
