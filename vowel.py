w=input("enter the word :")
v=['a','e','i','o','u']
wv=[]
for x in w:
    if(x in v and x not in wv):
        wv.append(x)
print("vowels in",w,"are:",wv)
