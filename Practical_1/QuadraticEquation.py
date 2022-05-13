#Find roots of Quadratic Equation
import math
a = int(input("Enter value of a "))
b = int(input("Enter value of b "))
c = int(input("Enter value of c "))
dis = b**2 - 4*a*c
val = math.sqrt(dis)
res1 = (-b + val)/2*a
res2 = (-b - val)/2*a

print("Values of Two root are ",res1,res2)
