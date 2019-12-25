inp=list(input())
inp.sort(key=lambda x:x.upper())
grp_list=list()
length=len(inp)
temp=""
index=0
while(index<length-1):
    if(inp[index]==inp[index+1] or inp[index]==inp[index+1].lower() or inp[index]==inp[index+1].upper()):
        temp+=inp[index]
        index+=1
    else:
        temp+=inp[index]
        grp_list.append(temp)
        temp=""
        index+=1
if(inp[index-1]==inp[index] or inp[index-1]==inp[index].lower() or inp[index-1]==inp[index].upper()):
    temp+=inp[index]
    grp_list.append(temp)
else:
    if(temp==""):
        grp_list.append(inp[index])
    else:
        grp_list.append(temp)
        grp_list.append(inp[index])
groups=len(grp_list)
if(groups%2==0):
    for i in range(0,groups//2):
        print(grp_list[i],end="",sep="")
        print(grp_list[groups-i-1],end="",sep="")
else:
    for i in range(0,groups//2):
        print(grp_list[i],end="",sep="")
        print(grp_list[groups-i-1],end="",sep="")
    print(grp_list[groups//2],end="",sep="")
