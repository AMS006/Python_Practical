#Python programme to check whether entered number in perfect number or not
import math as m
num = int(input("Enter a number "))
sum = 0
i = 1
while i<=num//2:
    sum = sum + i
    i=i+1
if(num==sum):
    print(num ," is perfect Number ")
