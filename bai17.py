import math
def check_snt(n):
    a =0
    for i in range(1,n+1):
        if(n%i==0):
            a =a+1
    if(a==2):
        return True
    return False
def find(a,b,c):
    x = 1
    sum = a+b+c
    while(check_snt(sum)!=True):
        x = x+1
        sum = a*(x**2)+b*x+c
    print(x)
a = int(input("nhap so a: "))
b = int(input("nhap so b: "))
c = int(input("nhap so c: "))
find(a,b,c)