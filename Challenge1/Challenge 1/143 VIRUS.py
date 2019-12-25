pi="141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067"
n=int(input())
res="";re=""
for i in range(0,len(pi),2):
    res+=pi[i]
    if(i!=len(pi)-1):
        re+=pi[i+1]
print("re",re)
print("res",res)
print("pi",pi)
print(re[n-1],res[n-1])
