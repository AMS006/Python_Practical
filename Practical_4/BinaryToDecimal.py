bin = int(input("Enter a Binary Number"))
ans = 0
i = 0
while bin!=0:
    ans += (bin%10)*((2) ** (i))
    bin = bin//10
    i=i+1
print(ans)
