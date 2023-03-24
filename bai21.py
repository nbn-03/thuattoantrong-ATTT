import math
def check_snt(n):
    a =0
    for i in range(1,n+1):
        if(n%i==0):
            a =a+1
    if(a==2):
        return True
    return False
def check_ssnt(n):
    dem = 0
    for i in range(1,n):
        if(check_snt(i)==True and check_snt(n)==True):
            dem = dem +1
    if(check_snt(dem)==True):
        return True
    return False
def find(a,b):
    dem = 0
    for i in range(a,b+1):
        if(check_ssnt(i)==True):
            dem = dem +1
            #print(i)
    print(dem)
a = int(input("nhap so a: "))
b = int(input("nhap so b: "))
find(a,b)