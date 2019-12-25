import math
#a=float(input())
hyp1=float(input())
hyp2=float(input())
ang1=float(input())
ang2=float(input())
#print(hyp1,',',math.degrees(math.asin(a/hyp1)))
#print(hyp2,',',math.degrees(math.acos(a/hyp2)))
#hyp1,ang1=hyp1,math.degrees(math.asin(a/hyp1))
#hyp2,ang2=hyp2,math.degrees(math.acos(a/hyp2))
hyp1=float(hyp1)
hyp2=float(hyp2)
ang1=float(ang1)
ang2=float(ang2)
Area1=(((hyp1)/2)**2)*(math.sin(math.radians(2*abs(ang1))))
Area2=(((hyp2)/2)**2)*(math.sin(math.radians(2*abs(ang2))))
if((ang1<0 and (ang2)>0) or ((ang1)>0 and (ang2)<0)):
    print((round((Area1+Area2))))
else:
    print(Area1,Area2)
    print((round((Area1+Area2))))
    print((round(abs(Area2-Area1))))
    
