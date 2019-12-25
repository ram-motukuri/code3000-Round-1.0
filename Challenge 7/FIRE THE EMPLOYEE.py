while(1):
    O,N,P=map(int,input().split())
    sal=[]
    for i in range(O):
        os,ns=map(int,input().split())
        sal.append(ns-os)
    nsal=list(map(int,input().split(",")))
    sal=sal+nsal
    sal.sort()
    no=0
    print(sal)
    for i in range(len(sal)):
        if(no<=P):
            no=no+sal[i]
        else:
            #print(no,sal[:i-1],sum(sal[:i-1]),len(sal[:i]))
            print(i-1)
            break
