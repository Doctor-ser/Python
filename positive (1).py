n=int(input("enter limit of array"))
num=[]
for i in range(n):
    item=int(input("enter the number"))
    num.append(item)
print("List",num)
print("positive numbers")
for x in num:
    if(x>0):
        print(x)
    elif(x==0):
        print("ZERO is neither positive or negative")
