import math 
a=int(input('enter the base side of the right triangle'))
b=int(input('enter the perpendicular side of the right triangle'))

#c= math.sqrt(pow(a,2)+pow(b,2))
c= math.sqrt(a*a+b*b)
print(f"{round(c,2)}cm")