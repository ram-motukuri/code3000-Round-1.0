import datetime 
import calendar 
def findDay(date):
    print(date)
    day, month, year = (int(i) for i in date.split(' '))     
    dayNumber = calendar.weekday(year, month, day) 
    days =["Monday", "Tuesday", "Wednesday", "Thursday", 
                         "Friday", "Saturday", "Sunday"] 
    return (days[dayNumber]) 

def smallest(lst):
    for i,n in enumerate(lst):  
        if n != '0':  
            tmp = lst.pop(i) 
            break 
    return str(tmp) + ''.join(lst)
n=int(input())
st =sorted(list(str(n)))
y=int(smallest(st[0:4]))
del st[0:4]
st=st[::-1]
if(0 not in st[0:2]):
    st=st[::-1]
    if(sum(list(map(int,st[0:2])))==3):
        m=12
        del st[0:2]
        st=st[::-1]
    elif(sum(list(map(int,st[0:2])))==2):
        m=11
        del st[0:2]
    else:
        st=st[::-1]
        m=int(st[0])
        del st[0:1]
elif(st[0:2].count(0)==1):
    if(sum(list(map(int,st[0:2])))==1):
        m=10
        del st[0:2]
st=st[::-1]
if(int("".join(st[0:2]))<30):
    d=int("".join(st[0:2]))
else:
    d=int(min(st))
date=" ".join([str(d),str(m),str(y)])
print(findDay(date)) 
        
        
