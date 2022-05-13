#Happy Number
def isHappy(n):
    temp = n
    sum = 0
    while temp>0:
        rem = temp%10
        sum = sum + pow(rem,2)
        temp = temp//10

    return sum

num = int(input('Enter a Number'))
temp = isHappy(num)
temp1 = 0
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

