x,q,o=input().split(" ")
x=int(x)
q=int(q)
o=int(o)
if(x>q and x>o):
    print(x)
elif(q>x and q>o):
    print(q)
else:
    print(o)
