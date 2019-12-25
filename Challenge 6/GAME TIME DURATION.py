import datetime as datetime
def timediff(S,E):
    ST=":".join(list(map(str,S)))
    ET=":".join(list(map(str,E)))
    ST=datetime.datetime.strptime(ST,'%H:%M:%S')
    ET=datetime.datetime.strptime(ET,'%H:%M:%S')
    TD=(ET-ST)
    sec=TD.total_seconds()
    return(int(sec))
def timetotal(sec):
    mint="00"
    hour="00"
    if(sec>=60):
        secs=str(sec%60)
        mint=str(sec//60)
        if(int(mint)>=60):
            hour=str(int(mint)//60)
            mint=str(int(mint)%60)
        timed=":".join([hour,mint,secs])
        timed=datetime.datetime.strptime(timed, '%H:%M:%S').time()
    return(timed)
nd=int(input())
total=0
tl=[]
for j in range(nd):
    tim=[]
    time=input()
    tim=list(map(lambda x:list(map(int,x.split(":"))),time.split()))
    tl.append(tim)
    tl.sort()
total=total+(timediff(tl[0][0],tl[0][1]))
high=tl[0][1]
for k in range(len(tl)-1):
    if(high>=tl[k+1][0]):
        if(high<=tl[k+1][1]):
            total=total+(timediff(high,tl[k+1][1]))
            high=tl[k+1][1]
    else:
        high=tl[k+1][0]
        if(high<=tl[k+1][1]):
            total=total+(timediff(high,tl[k+1][1]))
            high=tl[k+1][1]
print(timetotal(total))

        
    
        
        
    
