s=input("enter the sentence:")
w=s.split()
c=dict()
for word in w:
    if word in c:
        c[word]+=1
    else:
        c[word]=1
print(c)
