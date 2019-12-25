no_sn=int(input())
no_lad=int(input())
sn=list(map(int,input().split(",")))
lad=list(map(int,input().split(",")))
snlen=list(map(int,input().split(",")))
ladlen=list(map(int,input().split(",")))
snake={}
ladder={}
for i in range(no_sn):
    snake[sn[i]]=snlen[i]
for i in range(no_lad):
    ladder[lad[i]]=ladlen[i]
no_play=int(input())
dicelist=[]
for i in range(no_play):
    no_moves=int(input())
    dice=list(map(int,input().split(",")))
    dicelist.append(dice)
for i in dicelist:
    start=1
    print(end='\n')
    for j in i:
        print(start,j)
        start=start+j
        if(start<101):
            print(start)
            if(start in sn):
                print(start,snake[start],"snake")
                start=snake[start]
            elif(start in lad):
                print(start,ladder[start],"ladder")
                start=ladder[start]
        elif(start==100):
            print(start)
            break
        else:
            start=start-j
    print(start)

        
    
