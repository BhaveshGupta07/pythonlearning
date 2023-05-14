import sys
a = int(input("enter the first value"))
b = int(input("enter the second value"))
operator=input("enter the operator + - / * ")
if operator == "+":
    print(a+b)
elif operator =="-":
    print(a-b)
elif operator == "/":
    print(a/b)
elif operator == "*":
    print(a*b)
else:
    print("enter valid operator")
    
#sys.exit()
