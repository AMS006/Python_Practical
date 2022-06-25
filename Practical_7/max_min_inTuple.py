from tkinter.tix import MAX


list = list(map(int,input("Enter elements of tuples : ").split()))
tup = tuple(list)
max = tup[0]
min = tup[0]
for i in list:
    if(i < min):
        min = i
    elif(i > max):
        max = i
print ("Max Value is : ",max , "\nMin Value is : ",min)