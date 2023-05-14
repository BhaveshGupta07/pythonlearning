rows=int(input("enter number of rows "))
for i in range(rows):
    for k in range(1,rows-i):
        print(" ",end=" ")
    for j in range(i):
        print("*", end=" ")
    print(" ")