n = input('Enter a Number')
count = len(n);
x = int(n)
temp = x
sum = 0
while x>0:
    rem = x%10
    sum += pow(rem,count)
    x = x//10
if sum==temp:
    print('Number is armstrong')
else:
    print('Number is not armstrong')