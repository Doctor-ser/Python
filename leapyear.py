curr=int(input("enter current year"))
fut=int(input("enter future year"))
print("leap year")
for curr in range(curr,fut+1):
    if((curr%4==0)and curr%100!=0 or curr%400==0):
        print(curr)
