#Emre Çamlıca, 150210071
import math
x0=float(input("Input x0: "))
x1=float(input("Input x1: "))
max=int(input("Input the maximum number of iterations: "))

#Newton's Method
x=x0
f_x = 4*math.log(x) - x
err1=0
err2=0
print()
print("Newton Method: ")
for i in range(max):
    if(f_x==0):
        break
    f_x = 4*math.log(x) - x
    f_prime_x = 4/x - 1
    x_next = x - f_x/f_prime_x
    if(i%2 == 0):
        err1 = abs(x_next-x)
    else:
        err2 = abs(x_next-x)
    if(err1!=0 and err2!=0): 
        print("iteration",i+1,": x =" , x_next, ": error <=", abs(x_next-x), ": convergence rate =", min(err2/err1, err1/err2))
    else:
        print("iteration",i+1,": x =" , x_next, ": error <=", abs(x_next-x))
    x = x_next
    
    
#Secant Method
x_prev=x0
x=x1
f_x = 4*math.log(x) - x
print()
print("Secant Method: ")
for i in range(max):
    if(f_x==0):
        break
    f_x_prev = 4*math.log(x_prev) - x_prev
    f_x = 4*math.log(x) - x
    x_next = x - f_x * (x-x_prev)/(f_x - f_x_prev)
    x_prev = x
    if(i%2 == 0):
        err1 = abs(x_next-x)
    else:
        err2 = abs(x_next-x)
    if(err1!=0 and err2!=0): 
        print("iteration",i+1,": x =" , x_next, ": error <=", abs(x_next-x), ": convergence rate =", min(err2/err1, err1/err2))
    else:
        print("iteration",i+1,": x =" , x_next, ": error <=", abs(x_next-x))
    x = x_next