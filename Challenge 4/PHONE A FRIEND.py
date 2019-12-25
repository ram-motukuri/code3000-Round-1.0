def ind(x):
    for i in l:
        if x in i:
            return(str(2+l.index(i))+str(1+i.index(x)))
l=[['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
m=input()
m=m.lower()
ans=""
for i in m:
    ans=ans+ind(i)
print(ans)
    
