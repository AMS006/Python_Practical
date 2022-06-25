list = list(map(str,input("Enter the words of list : ").split()))
newList = []
word = input("Enter the word to be removed : ")
n = int(input("Enter the occurance of word to be removed : "))
for i in range(len(list)):
    if(i==n and list[i]==word):
        list.pop(i)
    
print("Removed word form the list ",list)
