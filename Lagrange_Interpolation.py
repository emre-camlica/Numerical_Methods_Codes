#Emre Çamlıca, 150210071
import math
x_array = []
y_array = []
L_x_array = []
L_c_array = []
L_divide_array = []
size=3

for i in range(size):
    x=input("input x value: ")
    y=input("y value: ") 
    x_array.append(x)
    y_array.append(y)

for i in range(size):
    L_divide_array.append(1)
    L_x_array.append(0)
    L_c_array.append(1)
    for j in range(size):
        if(j!=i):
            L_x_array[i]=float(L_x_array[i])-float(x_array[j])
            L_c_array[i]=float(L_c_array[i])*float(x_array[j])
            L_divide_array[i]=float(L_divide_array[i])*(float(x_array[i])-float(x_array[j]))

x_sq_coefficient=float(0)
x_coefficient=float(0)
const_coefficient=float(0)

for i in range(3):
    x_sq_coefficient=x_sq_coefficient + float(1)*float(y_array[i])/float(L_divide_array[i])
    x_coefficient=x_coefficient +   float(L_x_array[i])*float(y_array[i])/float(L_divide_array[i])
    const_coefficient=const_coefficient +   float(L_c_array[i])*float(y_array[i])/float(L_divide_array[i])
print("f(x) = ",  x_sq_coefficient, "x^2 + ", x_coefficient,  "x + ", const_coefficient)



