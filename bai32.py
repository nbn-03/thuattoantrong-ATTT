import math
import random
def check_prime(n):
    if n<=1:
        return False
    if n ==2:
        return True
    else:
        for i in range(2,math.ceil(math.sqrt(n))+1):
            if(n%i==0):
                return False
        return True
def find_gcd(a,b):
    if b==0:
        return a
    else:
        x2 = 1
        x1 = 0
        y2 = 0
        y1 = 1
        while(b>0):
            q= math.floor(a/b)
            r = a - b*q
            x = x2 - x1*q
            y = y2 - y1*q
            a = b
            b = r
            x2 = x1
            x1 = x
            y2 = y1
            y1 = y
            d = a
            x = x2
            y = y2
        return d
def binary(n):
    list = []
    while(n>0):
        a = int(float(n%2)) # Tinh phan du
        list.append(a) # Day phan du vao danh sach
        n = (n-a)/2 # Tinh phan thuong cho phep tinh tiep theo
    return list
def binhphcl(a,k,n):
    list = binary(k)
    b = 1
    if(k==0):
        return b
    else:
        A = a
        if(list[0]==1):
            b = a
        for i in range(1,len(list)):
            A = pow(A,2)%n
            if(list[i]==1):
                b = (A*b)%n
            else:
                b = b
        return b
def nghichdao(a,p):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while(u!=1):
        q = math.floor(v/u)
        r = v - q*u
        x = x2 - x1*q
        v = u 
        u = r
        x2 = x1
        x1 = x
    return(x1%p)
def find(SBD):
    p = 1
    q = 1
    while(check_prime(q)==False or check_prime(p)==False):
        q = random.randint(100,500)
        p = random.randint(100,500)
    n = q*p
    phi = (q-1)*(p-1)
    e = 0
    while(find_gcd(e,phi)!=1):
        e = random.randint(10000,phi)
    m = SBD+123
    d = nghichdao(e,phi)
    c = binhphcl(m,e,n)
    m = binhphcl(c,d,n)
    print(q, p, n, phi, e, d, c, m)
SBD = int(input("nhap SBD: "))
find(SBD)