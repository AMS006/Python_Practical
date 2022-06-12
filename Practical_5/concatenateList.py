list1 = list(map(str,input("Enter the Element of list1 ").split()))
list2 = list(map(str,input("Enter the element of list2 ").split()))

for i in list1:
    for j in list2:
        print(i+j,end = " ")
    print()