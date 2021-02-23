from math import *

try:
    from prettytable import PrettyTable
except BaseException:
    print("you may need run =>> python -m pip install -U prettytable <==")
    print("or any other way to install prettytable")
    
def f(x):
    return sqrt(1+x**2)*(sin(3*x+0.1)+cos(2*x+0.3))

def f_(x):
    return sqrt_(1+x**2,dU)*(sin_(3*x+0.1,dV)+cos_(2*x+0.3,dW))

def cos_(x,eps):
    res = 0
    k=0
    while True:
        a = (-1)**k*(x**(2*k))/factorial(2*k)
        if(abs(a) < eps):
            break
        res+=a
        k+=1
    return res

def sin_(x,eps):
    res = 0
    k=0
    while True:
        a = (-1)**k*(x**(2*k+1))/factorial(2*k+1)
        if(abs(a) < eps):
            break
        res+=a
        k+=1
    return res

def sqrt_(a,eps):
    x = max(a,1)
    while True:
        x1 = 1/2*(x+a/x)
        if(abs(x1-x) < eps):
            break
        x = x1
    return x
        

EPS = 10**(-6)
dU = EPS/(3*1.5)
dV = EPS/(3*1.4)
dW = EPS/(3*1.4)

t = PrettyTable(['x','f_exact','f_approx','error'])
i = 0.2
while(i <= 0.3+0.01):
    t.add_row(["{:.3}".format(i),
               f(i),
               f_(i),
               "{:e}".format(abs(f(i)-f_(i)))
    ])
    i+=0.01
print(t)
print("Malinowski Ilya #12")

