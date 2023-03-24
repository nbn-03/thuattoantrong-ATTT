import math
def ktsnt(n):
    a =0
    for i in range(1,n+1):
        if(n%i==0):
            a =a+1
    if(a==2):
        return True
    return False
def tinh(n):
    list = []
    p = 0
    for i in range(1,n+1):
        if(n%i==0):
            list.append(i)
            p = p+i
    s = len(list)
    k = 0
    q = 0
    for i in range(0,s):
        if(ktsnt(list[i])==True):
            k = k+1
            q = q +list[i]
    print(n+s-k-q+p)
n = int(input('Nhap vao so n: '))
tinh(n)