import math
def ktsnt(n):
    a =0
    for i in range(1,n+1):
        if(n%i==0):
            a =a+1
    if(a==2):
        return True
    return False
def inn(a,b):
    dem = 0
    for i in range(a,b+1):
        if(ktsnt(i)==True):
            dem = dem +1
    print(dem)
a = int(input('Nhap vao so a: '))
b = int(input('Nhap vao so b: '))
inn(a,b)