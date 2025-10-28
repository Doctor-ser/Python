r=[]
s=int(input("enter the starting range(4-digit number):"))
e=int(input("enter the ending range(4-digit number):"))
if s<1000 or e>9999 or s>e:
	print("invalid range please enter a valid 4-digit range")
else:
	for num in range(s,e+1):
		if num % 2 ==0:
			root=int(num**0.5)
			if root*root==num:
				r.append(num)
print("4-digit even perfect square numbers in the given range :")
print(r)
