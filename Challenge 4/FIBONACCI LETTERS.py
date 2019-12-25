def sd(k):
    k=list(k)
    p=sum(list(map(int,k)))
    if(len(str(p))==1):
        return p
    else:
        return sd(str(p))
j=input()
j=j.lower()
x=""
y=""
for i in j:
    x=x+str(ord(i)-96)
    z=sd(x)
    y=y+str(z)
print(y[::-1])
