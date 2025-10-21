c=int(input("enter the current year:"))
f=int(input("enter the future year:"))
print("Leap Years:")
for c in range(c,f+1):
    if((c%4==0) and c%100!=0 or c%400==0):
        print(c)
