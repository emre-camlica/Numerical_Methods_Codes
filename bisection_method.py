#Emre Çamlıca, 150210071

import site

a=float(input("Input a: "))
e=float(input("Input e: "))
#y represents a^(1/5)
y=pow(abs(a), 0.2)
if(a<0):
    y*=(-1)
#Special cases where power is equal to number itself
if y==0:
    print("x =", y)
    quit(0)
elif y==1 or y==-1:
    print("x =", y)
    quit(0)
#Forming the bounds such that a^(1/5) will be in between these numbers
if abs(a)>1:
    boundl=0
elif a>0 and a<1:
    boundl=1
else:
    boundl=-1
boundh=a

if boundl>boundh:
    temp=boundh
    boundh=boundl
    boundl=temp
    x=(boundh+boundl)/2
elif boundl<boundh:
    x=(boundh+boundl)/2

  
while abs(y-x)>e:
    if x>y:
        boundh=x
    elif x<y:
        boundl=x
    else:
        break
    x=(boundh+boundl)/2

print("x =",x)