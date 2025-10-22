list1=[]
list2=[]
m=int(input("ENTER THE LIMIT OF LIST1:"))
print("ENTER THE ELEMENTS:")
for i in range(0,m):
    value=int(input())
    list1.append(value)
n=int(input("ENTER THE LIMIT OF LIST2:"))
print("ENTER THE ELEMENTS:")
for i in range(0,n):
    value=int(input())
    list2.append(value)
print(list1,list2)
if(len(list1)==len(list2)):
    print("both list1 and list2 are same length")
else:
    print("both list1 and list2 are not of the same length")
if sum(list1)==sum(list2):
    print("The sum of both list1 and list2 are same")
else:
    print("The sum of both list1 and list2 are not same")
list3=[each for each in list1 if each in list2]
print("same members are:",list3)
