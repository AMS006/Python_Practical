list = [(1,2,3,4),"Python",('a','b','c','d'),15]

count = 0
for i in list:
    if(type(i) is tuple):
        count = count + 1
print(count)