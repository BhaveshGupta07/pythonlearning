def addiition(number1,number2):
    product = number1 * number2
    if product<=1000:
        return product
    else:
        return number1+number2;

number1=int(input( ))
number2=int(input( ))
result=addiition(number1,number2) 
print(result)