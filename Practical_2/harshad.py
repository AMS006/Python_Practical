n = int(input('Enter a Number'))
temp = n
sum = 0
while temp>0:
    rem = temp%10
    sum = sum + rem
    temp = temp//10

if((n%sum)==0):
    print('Number is Harshad number')
else:
    print("Number is not Harshad number")