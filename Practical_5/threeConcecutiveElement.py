list = list(map(int, input("Enter the elements of the array : ").split()))
x = len(list)
while i<(x-2):
    if(list[i]==list[i+1] and list[i]==list[i+2]):
        print(list[i])
        i = i+2
    i = i+1

