#Pronic Number
import math as m


n = int(input('Enter a Number'))
temp = n
b = False
for i in range(m.ceil(m.sqrt(n))):
    if (i * (i+1)==n):
        print('pronic number')
        b = True
if(b==False):
    print("Not pronic Number")
    

