#Python Program to convert Decimal number to Binary Number
num = int(input("Enter a Number "))
ans = ""
i = 0
while num!=0:
    i = num%2
    ans = ans + str(i)
    num = num//2

print(ans [::-1])