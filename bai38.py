import math
 
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
a = int(input("nhap so a: "))
p = int(input("nhap so p: "))
print(nghichdao(a,p))
