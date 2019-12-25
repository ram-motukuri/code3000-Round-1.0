from itertools import combinations
from itertools import product
def foo(nums):
    p=[]
    k= list(product(*([x, -x] for x in nums)))
    print(k)
    for i in range(len(k)//2):
        p.append(abs(sum(k[i])))
    print(p)
    return (p)
def score(a,n):
    comb=[]
    s=[]
    for i in range(1,n+1):
        comb=comb+list(combinations(a,i))
    print(comb)
    for i in comb:
        a=foo(list(i))
        s=s+a
    return (list(set(s)))
while(1):
    n=int(input())
    x=input()
    y=input()
    y=y.split(",")
    x=list(map(int,x.split(",")))
    sc=0
    for i in range(0,len(y),n):
        k=list(y[i:i+n])
        k=list(map(int,k))
        print(k)
        if x[i//n] not in score(k,n):
            print(i//n,x[i//n])
            sc=sc+x[i//n]
    print(sc)
