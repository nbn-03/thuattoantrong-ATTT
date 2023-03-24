import math
def check_snt(n):
    a =0
    for i in range(1,n+1):
        if(n%i==0):
            a =a+1
    if(a==2):
        return True
    return False
def find(n):
    for i in range(0,n-1):
        if(check_snt(i)==True and check_snt(i+2)==True):
            print(i, i+2)
n = int(input("Nhap vao so n: "))
find(n)