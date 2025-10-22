string=input("Enter String:")
n=len(string)
f=string[0]
l=string[n-1]
m=l+string[1:n-1]+f
print("modified string:",m)
