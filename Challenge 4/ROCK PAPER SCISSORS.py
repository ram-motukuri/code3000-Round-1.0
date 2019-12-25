game={'R':'S','P':'R','S':'P'}
n=int(input())
l=[0]*n
m=int(input())
for i in range(m):
    p=input().split()
    for j in range(n):
        if(j==0):
            l[j]=l[j]+p[1:].count(game[p[j]])
        elif(j==n-1):
            l[j]=l[j]+p[:j].count(game[p[j]])
        else:
            l[j]=l[j]+(p[:j]+p[(j+1):]).count(game[p[j]])
print(" ".join(list(map(str,l))))
        
