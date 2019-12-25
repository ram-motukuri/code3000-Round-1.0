def check(number):
    strnum=list(map(int,list(str(number))))
    length=len(strnum)
    if(length==1):
        return("T")
    else:
        for i in range(len(strnum)):
            if(int(strnum[i])>(sum(strnum[0:i])+sum(strnum[i+1:length]))):
                return("F")
            else:
                pass
    return("T")
n=int(input())
x=int(input())
l=[]
m=[]
for i in range(n):
    l.append(str(i+1))
for row in range(n):
    m.append([])
    for col in range(n):
        m[row].append(0)
for i in range(x):
    s=1
    if(s==1):
        b,a=input().split()
        c=round(int(a)/n,3)
        for i in range(n):
            if(l[i]==b):
                for j in range(n):
                    m[i][j]=round((m[i][j]+c),3)
    print(m)
for i in range(n):
    for j in range(n):
        if(i==j):
            m[i][j]=0
        elif(i<j):
            if(m[i][j]<m[j][i]):
                m[j][i]=m[j][i]-m[i][j]
                m[i][j]=0
            elif(m[i][j]==m[j][i]):
                m[i][j]=0
                m[j][i]=0
            else:
                m[i][j]=m[i][j]-m[j][i]
                m[j][i]=0
print(m)
for i in range(n):
    for j in range(n):
        print(check(int(round(m[i][j]))),end=" ")
    print()
        
