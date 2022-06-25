arr = []
n = int(input("Enter number of tuples"))
for i in range(n):
    list1 = list(map(int,input("Enter Elements of Tuple ").split()))
    arr.append(tuple(list1))

k = int(input("Enter value of k : "))
for i in arr:
    if(all(j%k==0 for j in i)):
        print(i)