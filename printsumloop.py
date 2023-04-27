n=int(input("enter the range n"))
prev=0
for i in range (n):
    sum=i+prev
    print(f"previous number ={prev}, next number = {i} ,sum= {sum}")
    prev=i
