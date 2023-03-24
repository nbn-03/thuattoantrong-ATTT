import math
def check_snt(n):
    a =0
    for i in range(1,n+1):
        if(n%i==0):
            a =a+1
    if(a==2):
        return True
    return False
def find(a,b,c,m,l):
    for i in range(m,l+1):
        if(check_snt(a*(i**2)+b*i+c)==True):
            print(i)     
a = int(input("nhap so a: "))
b = int(input("nhap so b: "))
c = int(input("nhap so c: "))
m = int(input("nhap so m: "))
l = int(input("nhap so l: "))
find(a,b,c,m,l)