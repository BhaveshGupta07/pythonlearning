b=int(input("enter the palindrome number ")) #let the palindrome number =101
print(f"original string {b}")
a=b #a=101
reverse = 0 #assign the reverse
while a > 0: #true for a
    reminder = a % 10 #remainder for a will be = 1
    reverse= (reverse * 10) + reminder #(0*10)+1
    a = a // 10 #this will return round of value of 101 = 10 then the loop continues
if b == reverse:
    print("this is palindrome")
else:
    print("false")
