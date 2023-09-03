#Emre Çamlıca, 150210071

import site

number = float(input("Enter a rational number: "))

if number<0:
    sign="1"
    number=abs(number)
elif number==0:
    print("The binary representation is: 00000000000000000000000000000000")
    quit(0)
else:
    sign="0"
        
#writing as 1,smth * 2^count
count = 0;
if number < 1:
    while number<1:
        number=number*2
        count=count-1
        
elif number > 2:
    while number>2:
        number = number/2
        count = count+1

if count<-126 or count >127:
    raise Exception("Number can't be represented.")
  
#convert count to exponent
count+=127

exponent=''
while count!=0 and len(exponent)<8:
    if count%2==0:
        count/=2
        exponent+="0"
    else: 
        count/=2
        count = int(count)
        exponent+="1"
            
while len(exponent)<8:
    exponent+="0"

exponent=exponent[8::-1]

#convert decimal part
mantista=''
number=number-1
while len(mantista)<=22:
    number*=2
    if number>=1:
        number-=1
        mantista+="1"
        
    else :
        mantista+="0"

#append the strings

binary = sign + exponent + mantista
print("The binary representation is: " + binary)