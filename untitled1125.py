def myfunc():
    x = 5
    y = 10
    print(x + y)

def myfunc():
    userfunc1 = int(input("Enter the first number: "))
    userfunc2 = int(input("Enter the second number: "))
    operation = input("do you want to:'add' 'subtract' 'multiply' 'divide'")
    if operation == "add":
        return add(userfunc1, userfunc2)
    if operation == "subtract":
        return sub(userfunc1, userfunc2)
    if operation == "multiply":
        return mult(userfunc1, userfunc2)
    if operation == "divide":
        return div(userfunc1, userfunc2)
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a//b
print(myfunc())