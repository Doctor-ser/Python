num=[]
n=int(input("enter the number of elements"))
print("enter list of integers")
for i in range(1,n+1):
    e=int(input())
    if(e>100):
        num.append("OVER")
    else:
        num.append(e)
print("Entered List:",num)
