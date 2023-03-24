import math
def check_snt(n):
    a =0
    for i in range(1,n+1):
        if(n%i==0):
            a =a+1
    if(a==2):
        return True
    return False
def find_uoc(n):
    dem1=0
    for i in range (1,n+1):
        if(n%i==0):
            dem1=dem1 + 1
    print(dem1)
def find_unt(n):
    dem2=0
    for i in range (1,n+1):
        if(n%i==0 and check_snt(i)==True):
            dem2=dem2 + 1
    print(dem2)
n = int(input("Nhap vao so n: "))
find_uoc(n)
find_unt(n)