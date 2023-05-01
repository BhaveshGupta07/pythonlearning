b=int(input("enter the palindrome number "))
print(f"original string {b}")
a=b
reverse = 0
while a > 0:
    reminder = a % 10
    reverse= (reverse * 10) + reminder
    a = a // 10
if b == reverse:
    print("palindrome")
else:
    print("false")
