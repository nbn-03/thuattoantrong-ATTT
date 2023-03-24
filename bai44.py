import math
import random
def nghichdao(a,p):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while(u!=1):
        q = math.floor(v/u)
        r = v - u*q
        x = x2 - x1*q
        v = u
        u = r
        x2 = x1
        x1 = x
    return(x1%p)
def main():
    A = []
    B = []
    p = int(input("nhap p: "))
    n = random.randint(1,p-1)
    print("n là:",n)
    for i in range(0,n):
        a = random.randint(1,p-2)
        A.append(a)
    print(A)
    for i in range(0,n):
        k = nghichdao(A[i],p)
        B.append(k)
    print(B)
main()
    