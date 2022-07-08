#Happy Number
def isHappy(n):
    sum = 0
    rem = 0
    while n>0:
        rem = n%10
        sum = sum + pow(rem,2)
        n = n//10

    return sum

num = int(input('Enter a Number'))
temp = isHappy(num)
temp1 = 0
while(temp!=1 and temp!=4):
   temp = isHappy(temp)
if(temp==1):
    print('Happy Number')
elif(temp==4):
    print('Not Happy Number')
else:
    while(temp>=10):
        temp = isHappy(temp)
        if(temp==1):
            print('Happy Number')
        elif temp==4:
            print('Not Happy')

