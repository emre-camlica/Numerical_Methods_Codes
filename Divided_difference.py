#Emre Çamlıca, 150210071
import math
x_array = []
fx_array = []
fdd = []

while True:
    x=input("input x value: ")
    fx=input("f(x) value: ")
    if x=="" or fx=="":
        break
    x_array.append(x)
    fx_array.append(fx)
    fdd.append(fx)
     
j=len(fdd)
for index in range(len(fx_array)-1):
    for i in range(j-1):
        fdd.append((float(fdd[i+1])-float(fdd[i]))/(float(x_array[i+index+1])-float(x_array[i])))
    fdd=fdd[j:] #removes the elements from the previous step
    print(index+1,"." ," divided differences: ", fdd)
    j=len(fdd)
    
