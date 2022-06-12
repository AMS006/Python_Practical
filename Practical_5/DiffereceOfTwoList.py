list1 = list(map(int,input("Enter Element of List1 ").split()))
list2 = list(map(int,input("Enter Element of List2 ").split()))

print(list((set(list1)-set(list2))))
print(list(set(list2)-set(list1)))