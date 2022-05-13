n = input('Enter a Number')
l = len(n)
x = int(n)
temp = int(n)
sum = 0
while temp>0:
    rem = temp%10
    sum += pow(rem,l)
    l = l-1
    temp = temp//10
if(sum ==x):
    print("Disarium Number")
else:
    print("Number is not Disarium")
