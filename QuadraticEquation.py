import math
a = 1
b = 5
c = 6
dis = b**2 - 4*a*c
val = math.sqrt(dis)
res1 = (-b + val)/2*a
res2 = (-b - val)/2*a

print(res1,res2)
